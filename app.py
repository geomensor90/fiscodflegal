import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium
from shapely.geometry import Point
import os
import json

# Limpa o cache de dados
st.cache_data.clear()

# Limpa o cache de recursos (ex.: conexões, objetos grandes, etc.)
st.cache_resource.clear()

# Configurações iniciais
st.set_page_config(page_title="Detector de Shapefiles", layout="wide")
st.title("🗺️ Localizador de Polígonos")

# Coordenadas padrão de Brasília
DEFAULT_LAT = -15.614039
DEFAULT_LON = -47.666706

# Inicializar variáveis de sessão para coordenadas
if 'lat' not in st.session_state:
    st.session_state.lat = DEFAULT_LAT
if 'lon' not in st.session_state:
    st.session_state.lon = DEFAULT_LON

# Widgets de entrada
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Latitude", value=st.session_state.lat, format="%.6f", key="lat_input")
with col2:
    lon = st.number_input("Longitude", value=st.session_state.lon, format="%.6f", key="lon_input")

# Atualizar sessão se os inputs foram alterados manualmente
if lat != st.session_state.lat or lon != st.session_state.lon:
    st.session_state.lat = lat
    st.session_state.lon = lon
    st.rerun()

# Pasta dos shapefiles
SHAPEFILE_DIR = "shapefiles"

# Função melhorada para carregar shapefiles
@st.cache_data(persist=True, show_spinner="Carregando shapefiles...")
def load_all_shapefiles(directory):
    shapefiles = {}
    loaded_files = []
    
    for file in os.listdir(directory):
        if file.endswith(".shp"):
            try:
                path = os.path.join(directory, file)
                name = os.path.splitext(file)[0]
                gdf = gpd.read_file(path)
                
                # Verificar se tem geometrias válidas
                if not gdf.empty and 'geometry' in gdf.columns:
                    shapefiles[name] = gdf
                    loaded_files.append(file)
                else:
                    st.warning(f"Arquivo {file} não contém geometrias válidas")
            except Exception as e:
                st.error(f"Falha ao carregar {file}: {str(e)}")
    
    st.session_state['loaded_files'] = loaded_files
    return shapefiles

# Carregar shapefiles
if os.path.exists(SHAPEFILE_DIR):
    shapefiles = load_all_shapefiles(SHAPEFILE_DIR)
    if not shapefiles:
        st.error("Nenhum shapefile válido encontrado na pasta!")
        st.stop()
else:
    st.error(f"Diretório '{SHAPEFILE_DIR}' não existe!")
    st.stop()

# Criar mapa
m = folium.Map(
    location=[st.session_state.lat, st.session_state.lon],
    zoom_start=16,
    name='Satélite (Google Earth)',
    #tiles='https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}',
    attr='Google Earth',
    control_scale=True
)

# Adicionar controle de camadas para alternar entre satélite e mapa
folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}',
    attr='Google Maps',
    name='Mapa de Ruas'
).add_to(m)


folium.TileLayer(
    tiles='https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}',
    attr='Google Híbrido',
    name='Híbrido (Satélite + Ruas)'
).add_to(m)

folium.LayerControl().add_to(m)

# Adicionar evento de clique para capturar coordenadas
m.add_child(folium.LatLngPopup())

ponto = Point(st.session_state.lon, st.session_state.lat)
folium.Marker(
    [st.session_state.lat, st.session_state.lon],
    tooltip="Seu ponto",
    icon=folium.Icon(color="red", icon="map-pin")
).add_to(m)

# Processar interação com o mapa
map_interaction = st_folium(m, width=1200, height=600, returned_objects=["last_clicked"])

# Atualizar coordenadas se o usuário clicar no mapa
if map_interaction and map_interaction.get("last_clicked"):
    clicked_lat = map_interaction["last_clicked"]["lat"]
    clicked_lon = map_interaction["last_clicked"]["lng"]
    
    # Atualizar valores na sessão
    st.session_state.lat = clicked_lat
    st.session_state.lon = clicked_lon
    st.rerun()

# Processamento principal
if st.button("📄 Gerar Relatório 📄", type="primary"):
    resultados = []
    
    with st.status("Analisando polígonos...", expanded=True) as status:
        for name, gdf in shapefiles.items():
            try:
                # Converter para WGS84 se necessário
                if gdf.crs is None or not gdf.crs.is_geographic:
                    gdf = gdf.to_crs("EPSG:4326")
                
                # Verificar cada polígono
                for idx, row in gdf.iterrows():
                    if row['geometry'].contains(ponto):
                        # Extrair atributos
                        info = {
                            "Shapefile": name,
                            "ID_Polígono": idx,
                            **{col: row[col] for col in gdf.columns if col != 'geometry'}
                        }
                        resultados.append(info)
                        
                        # Destacar no mapa
                        folium.GeoJson(
                            row['geometry'],
                            tooltip=f"{name} | ID: {idx}",
                            style_function=lambda x: {
                                'fillOpacity': 0.015,
                                'weight': 2
                            }
                        ).add_to(m)
                        
            except Exception as e:
                st.error(f"Erro no shapefile {name}: {str(e)}")
        
        #status.update(label="Informações Geradas!", state="complete")
    
    # Mostrar resultados
    if resultados:
        st.success(f"✅ O ponto informado está inserido em {len(resultados)} polígono(s)")
        df = pd.DataFrame(resultados)

        if not df.empty:
            st.header("Relatório de Localização Geográfica")
            
            for _, row in df.iterrows():
                # Zoneamento do Distrito Federal
                if row['Shapefile'] == 'zoneamento_do_distrito_federal':
                    # Exibir o título uma vez
                    st.subheader("Zoneamento do Distrito Federal")
                    
                    # Exibir as informações, se existirem
                    if 'macroarea' in row:
                        st.write(f"Macro Área: {row['macroarea']}")
                    if 'macrozona' in row:
                        st.write(f"Macro Zona: {row['macrozona']}")
                    if 'sigla' in row:
                        st.write(f"Sigla: {row['sigla']}")
                
                # Diretrizes Urbanísticas Específicas DIUPE
                elif row['Shapefile'] == 'diretrizes_urbanisticas_especificas_diupe':
                    # Exibir o título uma vez
                    st.subheader("Diretrizes Urbanísticas Específicas DIUPE")
                    
                    # Exibir as informações, se existirem
                    if 'di_nome' in row:
                        st.write(f"Nome: {row['di_nome']}")
                    if 'di_process' in row:
                        st.write(f"Número do Processo: {row['di_process']}")
                    if 'di_link' in row:
                        st.write(f"Link do Processo: {row['di_link']}")

                # Zoneamento Das Diretrizes Urbansticias
                elif row['Shapefile'] == 'zoneamento_das_diretrizes_urbanisticas':
                    # Exibir o título uma vez
                    st.subheader("Zoneamento Das Diretrizes Urbansticias")
                    
                    # Exibir as informações, se existirem
                    if 'etuz_zona' in row:
                        st.write(f"Zona: {row['etuz_zona']}")

                # Novos Parcelamentos
                elif row['Shapefile'] == 'novos_parcelamentos':
                    # Exibir o título uma vez
                    st.subheader("Novos Parcelamentos")
                    
                    # Exibir as informações, se existirem
                    if 'upar_statu' in row:
                        st.write(f"Status: {row['upar_statu']}")
                    if 'upar_diupe' in row:
                        st.write(f"DIUPE: {row['upar_diupe']}")
                    if 'upar_diurb' in row:
                        st.write(f"DIURB: {row['upar_diurb']}")
                    if 'upar_propr' in row:
                        st.write(f"Natureza da propriedade: {row['upar_propr']}")
                    if 'upar_modal' in row:
                        st.write(f" Tipo: {row['upar_modal']}")
                    if 'upar_nm_pa' in row:
                        st.write(f"Nome: {row['upar_nm_pa']}")
                    if 'upar_num_p' in row:
                        st.write(f"Número do Processo: {row['upar_num_p']}")
            
        # Ordenar por shapefile e ID
        df = df.sort_values(by=['Shapefile', 'ID_Polígono'])
        
        # Mostrar tabela com scroll
        #st.dataframe(
        #    df,
        #    height=min(400, 35 * (len(df) + 1)),
        #    use_container_width=True
        #)
        
        # Opção para exportar
        st.download_button(
            "💾 Exportar para CSV",
            df.to_csv(index=False).encode('utf-8'),
            "resultados_ponto.csv",
            "text/csv"
        )
    else:
        st.warning("Nenhum polígono encontrado contendo o ponto")

# Adiciona controle de camadas
folium.LayerControl().add_to(m)

# Dados JSON fornecidos
data = {
  "Macrozona Urbana": {
    "Ocupação Regular": {
      "Com Diretriz": {
        "Terras Públicas - Desapropriadas": {
          "Sem Parcelamento": 1,
          "Parcelamento de Fato": 4,
          "Parcelamento Aprovado": 2,
          "Parcelamento Registrado": 1
        },
        "Terras Privadas - Não Desapropriadas": {
          "Sem Parcelamento": 2,
          "Parcelamento de Fato": 8,
          "Parcelamento Aprovado": 4,
          "Parcelamento Registrado": 2
        },
        "Terras Públicas/Privadas - Desapropriadas em Comum": {
          "Sem Parcelamento": 3,
          "Parcelamento de Fato": 12,
          "Parcelamento Aprovado": 6,
          "Parcelamento Registrado": 3
        }
      },
      "Sem Diretriz": {
        "Terras Públicas - Desapropriadas": {
          "Sem Parcelamento": 2,
          "Parcelamento de Fato": 8,
          "Parcelamento Aprovado": 4,
          "Parcelamento Registrado": 2
        },
        "Terras Privadas - Não Desapropriadas": {
          "Sem Parcelamento": 4,
          "Parcelamento de Fato": 16,
          "Parcelamento Aprovado": 8,
          "Parcelamento Registrado": 4
        },
        "Terras Públicas/Privadas - Desapropriadas em Comum": {
          "Sem Parcelamento": 6,
          "Parcelamento de Fato": 24,
          "Parcelamento Aprovado": 12,
          "Parcelamento Registrado": 6
        }
      }
    },
    "Ocupação Irregular com Área de regularização ": {
      "Com Diretriz": {
        "Terras Públicas - Desapropriadas": {
          "Sem Parcelamento": 9,
          "Parcelamento de Fato": 36,
          "Parcelamento Aprovado": 18,
          "Parcelamento Registrado": 9
        },
        "Terras Privadas - Não Desapropriadas": {
          "Sem Parcelamento": 18,
          "Parcelamento de Fato": 72,
          "Parcelamento Aprovado": 36,
          "Parcelamento Registrado": 18
        },
        "Terras Públicas/Privadas - Desapropriadas em Comum": {
          "Sem Parcelamento": 27,
          "Parcelamento de Fato": 108,
          "Parcelamento Aprovado": 54,
          "Parcelamento Registrado": 27
        }
      },
      "Sem Diretriz": {
        "Terras Públicas - Desapropriadas": {
          "Sem Parcelamento": 18,
          "Parcelamento de Fato": 72,
          "Parcelamento Aprovado": 36,
          "Parcelamento Registrado": 18
        },
        "Terras Privadas - Não Desapropriadas": {
          "Sem Parcelamento": 36,
          "Parcelamento de Fato": 144,
          "Parcelamento Aprovado": 72,
          "Parcelamento Registrado": 36
        },
        "Terras Públicas/Privadas - Desapropriadas em Comum": {
          "Sem Parcelamento": 54,
          "Parcelamento de Fato": 216,
          "Parcelamento Aprovado": 108,
          "Parcelamento Registrado": 54
        }
      }
    }
  }
}

def main():
    st.title("GRAVIDADE TERRITORIAL")
    
    # Nível 1: Macrozona
    macrozona_options = list(data.keys())
    selected_macrozona = st.selectbox("Selecione a Macrozona:", macrozona_options)
    
    if selected_macrozona:
        # Nível 2: Tipo de Ocupação
        ocupacao_options = list(data[selected_macrozona].keys())
        selected_ocupacao = st.selectbox("Selecione o Tipo de Ocupação:", ocupacao_options)
        
        if selected_ocupacao:
            # Nível 3: Diretriz
            diretriz_options = list(data[selected_macrozona][selected_ocupacao].keys())
            selected_diretriz = st.selectbox("Selecione a Diretriz:", diretriz_options)
            
            if selected_diretriz:
                # Nível 4: Tipo de Terras
                terras_options = list(data[selected_macrozona][selected_ocupacao][selected_diretriz].keys())
                selected_terras = st.selectbox("Selecione o Tipo de Terras:", terras_options)
                
                if selected_terras:
                    # Nível 5: Parcelamento
                    parcelamento_options = list(data[selected_macrozona][selected_ocupacao][selected_diretriz][selected_terras].keys())
                    selected_parcelamento = st.selectbox("Selecione o Tipo de Parcelamento:", parcelamento_options)
                    
                    if selected_parcelamento:
                        # Mostrar o valor correspondente
                        valor = data[selected_macrozona][selected_ocupacao][selected_diretriz][selected_terras][selected_parcelamento]
                        st.success(f"Valor selecionado: {valor}")
                        
                        # Mostrar o caminho completo selecionado
                        #st.subheader("Caminho selecionado:")
                        #st.write(f"Macrozona: {selected_macrozona}")
                        #st.write(f"Ocupação: {selected_ocupacao}")
                        #st.write(f"Diretriz: {selected_diretriz}")
                        #st.write(f"Terras: {selected_terras}")
                        #st.write(f"Parcelamento: {selected_parcelamento}")
                        #st.write(f"Valor: {valor}")

if __name__ == "__main__":
    main()
