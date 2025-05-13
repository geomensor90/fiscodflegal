import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from streamlit_folium import st_folium
from shapely.geometry import Point
import os

# Configurações iniciais
st.set_page_config(page_title="Detector de Shapefiles", layout="wide")
st.title("🗺️ Localizador de Polígonos")

# Coordenadas padrão de Brasília
DEFAULT_LAT = -15.817533
DEFAULT_LON = -47.978620

# Widgets de entrada
col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("Latitude", value=DEFAULT_LAT, format="%.6f")
with col2:
    lon = st.number_input("Longitude", value=DEFAULT_LON, format="%.6f")

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

# Mostrar arquivos carregados
with st.expander("📁 Shapefiles carregados", expanded=False):
    st.write(f"Total de shapefiles: {len(shapefiles)}")
    st.json(st.session_state.get('loaded_files', []))

# Criar mapa
m = folium.Map(location=[lat, lon], zoom_start=16)
ponto = Point(lon, lat)
folium.Marker(
    [lat, lon],
    tooltip="Seu ponto",
    icon=folium.Icon(color="red", icon="map-pin")
).add_to(m)

# Processamento principal
if st.button("🔍 Procurar em todos os shapefiles", type="primary"):
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
        
        status.update(label="Análise concluída!", state="complete")
    
    # Mostrar resultados
    if resultados:
        st.success(f"✅ Encontrado em {len(resultados)} polígono(s)")
        df = pd.DataFrame(resultados)

        if not df.empty:
            # --------------------------------------------------
            # NOVO CÓDIGO PARA MOSTRAR INFORMAÇÕES ESPECÍFICAS
            # --------------------------------------------------
            st.subheader("Informações do Polígono")
            
            for _, row in df.iterrows():
                if row['Shapefile'] == 'conjunto' and 'cj_conjunt' in row:
                    st.write(f"Conjunto: {row['cj_conjunt']}")
                    
                if row['Shapefile'] == 'AREA_IMOVEL_1' and 'cod_tema' in row:
                    st.write(f"CAR: {row['cod_tema']}")
            
            # Adicione mais condições conforme necessário para outros shapefiles
            # --------------------------------------------------


        
        
        # Ordenar por shapefile e ID
        df = df.sort_values(by=['Shapefile', 'ID_Polígono'])
        
        # Mostrar tabela com scroll
        st.dataframe(
            df,
            height=min(400, 35 * (len(df) + 1)),
            use_container_width=True
        )
        
        # Opção para exportar
        st.download_button(
            "💾 Exportar para CSV",
            df.to_csv(index=False).encode('utf-8'),
            "resultados_ponto.csv",
            "text/csv"
        )
    else:
        st.warning("Nenhum polígono encontrado contendo o ponto")
# Configuração otimizada do WMS
# Cria mapa centrado no DF




# Adiciona controle de camadas
folium.LayerControl().add_to(m)

# Mostrar mapa
st_folium(m, width=1200, height=600, returned_objects=[])



