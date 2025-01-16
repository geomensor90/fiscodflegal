import streamlit as st
import pandas as pd

# Dados fornecidos
dados = {
    "Ano": [2020, 2021, 2022, 2023, 2024, 2025],
    "Coluna 2": [1.71, 1.8, 2, 2.12, 2.2, 2.31],
    "Coluna 3": [0.23, 0.24, 0.27, 0.29, 0.3, 0.31]
}

df = pd.DataFrame(dados)

# Título do app
st.title("Taxa de Execução de Obras (TEO)")

# Primeiro campo: entrada numérica
campo1 = st.number_input("Insira a área da construção em m²:", min_value=0.0, step=1.0, format="%.2f")

# Segundo campo: seleção dos anos (como checkboxes)
anos_selecionados = []
st.subheader("Selecione os anos:")
for ano in df["Ano"]:
    if st.checkbox(str(ano)):
        anos_selecionados.append(ano)

# Checkbox para Art. 28
artigo_28 = st.checkbox("Art. 28. Sujeitar-se-á à multa de 100% (cem por cento) sobre o valor atualizado da taxa devida o contribuinte que não prestar, no prazo estabelecido, a declaração prevista no art. 25, ou o fizer com omissão ou inexatidão.")

# Checkbox para Art. 27
artigo_27 = st.checkbox("Art. 27. Isentos do pagamento da Taxa de Execução de Obras")

if artigo_27:
    st.markdown("""
    <div style="text-align: center; font-size: 16px;">   
    <strong>I</strong> – a União, os Estados, o Distrito Federal e os Municípios;<br>
    <strong>II</strong> – as obras em prédios sedes de embaixadas;<br>
    <strong>III</strong> – as autarquias e fundações públicas, para as obras que realizarem em prédios destinados às suas finalidades específicas, excluídas as destinadas à revenda ou locação e as utilizadas para fins estranhos a essas pessoas jurídicas;<br>
    <strong>IV</strong> – as obras em imóveis reconhecidos em lei como de interesse histórico, cultural ou ecológico, desde que respeitem integralmente as características arquitetônicas originais das fachadas;<br>
    <strong>V</strong> – as obras executadas por imposição do Poder Público;<br>
    <strong>VI</strong> – as sedes de partidos políticos;<br>
    <strong>VII</strong> – as sedes das entidades sindicais;<br>
    <strong>VIII</strong> – templos de qualquer culto;<br>
    <strong>IX</strong> – o beneficiário de programa habitacional realizado pelo Poder Público, com área máxima de construção de 120m² em lote de uso residencial unifamiliar, que não seja possuidor de outro imóvel residencial no Distrito Federal;<br>
    <strong>X</strong> – as obras que independam de licença ou comunicação para serem executadas, de acordo com o Código de Edificações do Distrito Federal;<br>
    <strong>XI</strong> – as entidades associativas ou cooperativas de trabalhadores.<br>
    <strong>Parágrafo único:</strong> A efetivação do benefício de que trata este artigo se dará na forma do regulamento, mediante requerimento acompanhado de documentação comprobatória.
    </div>
    """, unsafe_allow_html=True)


# Verifica se anos foram selecionados
if anos_selecionados:
    # Filtra os dados pelos anos selecionados
    dados_filtrados = df[df["Ano"].isin(anos_selecionados)]

    # Calcula os resultados com base no valor do campo1
    resultados = []
    soma_total = 0
    for _, row in dados_filtrados.iterrows():
        if campo1 <= 1000:
            resultado = campo1 * row["Coluna 2"]
        else:
            resultado = campo1 * row["Coluna 2"] + campo1 * row["Coluna 3"]
        resultados.append((row["Ano"], resultado))
        soma_total += resultado

    # Aplica a multa de 100% se Art. 28 for selecionado
    if artigo_28:
        soma_total *= 2

    # Aplica a multa de 0% se Art. 27 for selecionado
    if artigo_27:
        soma_total *= 0

    # Exibe os resultados
    st.subheader("Resultados")
    for ano, resultado in resultados:
        st.write(f"Ano {ano:.0f}: R$ {resultado:.2f}")

    # Exibe a soma total
    st.subheader("Soma Total")
    st.write(f"R$ {soma_total:.2f}")
else:
    st.warning("Por favor, selecione ao menos um ano.")

"""
import streamlit as st
# Função para exibir a legislação com base na situação e ação selecionada
def obter_legislacao(situacao, acao):
    legislacao_infringida = situacoes[situacao]['legislacao_infringida']
    
    artigos_acao = situacoes[situacao]['acoes']

    if acao in artigos_acao:
        return legislacao_infringida, artigos_acao[acao]
    else:
        return legislacao_infringida, "Selecione uma ação válida."

# Dicionário com as situações e dados
situacoes = {
    'Executar obra de habitação unifamiliar sem o acompanhamento e registro profissional': {
        'nome': 'Executar obra de habitação unifamiliar sem o acompanhamento e registro profissional',
        'nivel': 'Leve',
        'legislacao_infringida': 'Arts. 15, I, II, VI, 53-A da Lei nº 6.138/2018. Arts. 68, VI da Dec nº 43.056/2022',
        'Motivo Fiscal': {
            '1. Ausência de profissional habilitado': 'LICENCIAMENTO - 1. Ausência de profissional habilitado',
            '2. Ausência de documento de Responsabilidade Técnica': 'LICENCIAMENTO - 2. Ausência de documento de Responsabilidade Técnica',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, 117, 122, 123, §1º, I, 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §1º, I, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177,190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Arts. 13, 116, 117, 122, 123, §1º, I, 124 V ,133, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180, 181 e 197 do Dec. 43.056/2022',
            'Auto de Apreensão': 'Arts. 13, 116, 117, 122, 123, §1º, I, 124 VI, 134, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 VI, 182, 190 e 197 do Dec.43.056/2022',
            'Interdição': 'Arts. 13, 116, 117, 122, 123, §1º, I, 124 IV, 132, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 IV, 178, 179, 190 e 197 do Dec. 43.056/2022',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §1º, I, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 e 197 do Dec. 43.056/2022',
        }
    },
    'Depositar materiais de construção e equipamentos em área pública, sem autorização': {
        'nome': 'Depositar materiais de construção e equipamentos em área pública, sem autorização',
        'nivel': 'Leveeve',
        'legislacao_infringida': 'Arts. 15, VII, 85, I, III e IV da Lei nº 6.138/2018. Arts. 115 da Dec nº 43.056/2022',
        'Motivo Fiscal': {
            '1. Falta de Licença Específica': 'CANTEIRO DE OBRAS - 1. Falta de Licença Específica',
            '2. Descumprimento de Plano de Gerenciamento de Resíduos da Construção Civil': 'CANTEIRO DE OBRAS - 2. Descumprimento de Plano de Gerenciamento de Resíduos da Construção Civil',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, 117, 122, 123, §1º, II 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §1º, II, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177, 190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Arts. 13, 116, 117, 122, 123, §1º, II, 124 V ,133, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180, 181 e 197 do Dec. 43.056/2022',
            'Auto de Apreensão': 'Arts. 13, 116, 117, 122, 123, §1º, II, 124 VI, 134, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 VI, 182, 190 e 197 do Dec. 43.056/2022',
            'Interdição': 'Arts. 13, 116, 117, 122, 123, §1º, II, 124 IV, 132, 135 e 136 da Lei nº 6.138/2012018. Arts 10, 167, 168 IV, 178, 179, 190 e 197 do Dec. 43.056/2022',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §1º, II, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 e 197 do Dec. 43.056/2022',
        }
    },
    'Deixar de manter, no canteiro de obras, placa informativa de dados técnicos do projeto e obra': {
        'nome': 'Deixar de manter, no canteiro de obras, placa informativa de dados técnicos do projeto e obra',
        'nivel': 'Leve',
        'legislacao_infringida': 'Arts. 15, IV e XI da Lei nº 6.138/2018. Arts. 108 e 163 da Dec nº 43.056/2022',
        'Motivo Fiscal': {
            '1. Falta de Placa Informativa fixada em local visível': 'CANTEIRO DE OBRAS - 1. Falta de Placa Informativa fixada em local visível',
            '2. Placa informativa sem todos os dados da obra e de Responsáveis Técnicos': 'CANTEIRO DE OBRAS - 2. Placa informativa sem todos os dados da obra e de Responsáveis Técnicos',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, 117, 122, 123, §1º, III, 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §1º, III, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177, 190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Não cabe',
            'Auto de Apreensão': 'Não cabe',
            'Interdição': 'Não cabe',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §1º, III, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 e 197 do Dec. 43.056/2022',
        }
    },

#4
    'Deixar de comunicar à fiscalização a paralisação da obra': {
        'nome': 'Deixar de comunicar à fiscalização a paralisação da obra',
        'nivel': 'Leve',
        'legislacao_infringida': 'Arts. 18, IV da Lei nº 6.138/2018. Arts. 11, § 2º da Dec nº 43.056/2022',
        'Motivo Fiscal': {
            '1. Obra licenciada paralisada sem comunicação ao DF-Legal': 'FISCALIZAÇÂO - 1. Obra licenciada paralisada sem comunicação ao DF-Legal',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, , 122, 123, §1º, IV, 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §1º, IV, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177, 190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Não cabe',
            'Auto de Apreensão': 'Arts. 13, 116, 117, 122, 123, §1º, IV, 124 VI, 134, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 VI, 182, 190 e 197 do Dec. 43.056/2022',
            'Interdição': 'Arts. 13, 116, 117, 122, 123, §1º, IV, 124 IV, 132, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 IV, 178, 179, 190 e 197 do Dec. 43.056/2022',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §1º, IV, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 e 197 do Dec. 43.056/2022',
        }
    },

#5
    'Descumprir os termos do licenciamento de canteiro de obras e estandes de vendas': {
        'nome': 'Descumprir os termos do licenciamento de canteiro de obras e estandes de vendas',
        'nivel': 'Leve',
        'legislacao_infringida': 'Arts. 15, III, 51, 54, I, IV, 59, 67, §4º, 71 I, IV, 78, 79 e 81 da Lei nº 6.138/2018. Arts. 69, 70, 71, 90, 109, 111 a 114 e 118 a 120 da Dec nº 43.056/2022',
        'Motivo Fiscal': {
            '1. Descumprimento do Alvará de Construção': 'LICENCIAMENTO E CANTEIRO DE OBRAS - 1. Descumprimento do Alvará de Construção',
            '2. Descumprimento da Licença Específica': 'LICENCIAMENTO E CANTEIRO DE OBRAS - 2. Descumprimento da Licença Específica',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, 117, 122, 123, §1º, V, 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §1º, V, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177, 190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Não cabe',
            'Auto de Apreensão': 'Arts. 13, 116, 117, 122, 123, §1º, V, 124 VI, 134, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 VI, 182, 190 e 197 do Dec. 43.056/2022',
            'Interdição': 'Arts. 13, 116, 117, 122, 123, §1º, V, 124 IV, 132, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 IV, 178, 179, 190 e 197 do Dec. 43.056/2022',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §1º, V, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176, 190 e 197 do Dec. 43.056/2022',
        }
    },

#6
    'Executar obras ou manter edificações passíveis de regularização, localizadas em área privada, sem licença ou em desacordo com o projeto habilitado': {
        'nome': 'Executar obras ou manter edificações passíveis de regularização, localizadas em área privada, sem licença ou em desacordo com o projeto habilitado',
        'nivel': 'Média',
        'legislacao_infringida': 'Arts. 14, 15, III, 20, 22 e 50 da Lei nº 6.138/2018. Arts. 77 a 84 do Dec nº 43.056/2022',
        'Motivo Fiscal': {
            '1. Falta de Alvará de Construção;': '1. Falta de Alvará de Construção;',
            '2. Obra em desacordo com Projeto Habilitado': '2. Obra em desacordo com Projeto Habilitado',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, 117, 122, 123, §2º, I, 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §2º, I, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177. 190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Não cabe',
            'Auto de Apreensão': 'Arts. 13, 116, 117, 122, 123, §2º, I, 124 VI, 134, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 VI, 182, 190 e 197 do Dec. 43.056/2022',
            'Interdição': 'Arts. 13, 116, 117, 122, 123, §2º, I, 124 IV, 132, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 IV, 178, 179, 190 e 197 do Dec. 43.056/2022',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §2º, I, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 e 197 do Dec. 43.056/2022',
        }
    },

#7
    'Causar impedimento ou embaraço à atividade de fiscalização': {
        'nome': 'Causar impedimento ou embaraço à atividade de fiscalização',
        'nivel': 'Média',
        'legislacao_infringida': 'Arts. 15, V da Lei nº 6.138/2018',
        'Motivo Fiscal': {
            '1. Dificultar fiscalização a: (a) Acessar a obra; (b) Acessar os documentos de licenças, autorizações e ART, (c) Registro fotográfico e outros; (d) Constranger ao Auditor em sua atividade; (e) Não responder ao chamado.': 'DESVIO DE CONDUTA E FISCALIZAÇÃO - 1. Dificultar fiscalização a: (a) Acessar a obra; (b) Acessar os documentos de licenças, autorizações e ART, (c) Registro fotográfico e outros; (d) Constranger ao Auditor em sua atividade; (e) Não responder ao chamado.',
        },
        'acoes': {
            'Auto de Notificação': 'Arts. 13, 116, 117, 122, 123, §2º, II, 124 I, 125 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170, 171 e 197 do Dec. 43.056/2022',
            'Auto de Embargo': 'Arts. 13, 116, 117, 122, 123, §2º, II, 124 III, 131 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 III, 177, 190 e 197 do Dec. 43.056/2022',
            'Intimação Demolitória': 'Não cabe',
            'Auto de Apreensão': 'Arts. 13, 116, 117, 122, 123, §2º, II, 124 VI, 134, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 VI, 182, 190 e 197 do Dec. 43.056/2022',
            'Interdição': 'Arts. 13, 116, 117, 122, 123, §2º, II, 124 IV, 132, 135 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168 IV, 178, 179, 190 e 197 do Dec. 43.056/2022',
            'Auto de Infração': 'Arts. 13, 116, 117, 122, 123, §2º, II, 124, II, 126, I, 127, 128 e 136 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 e 197 do Dec. 43.056/2022',
        }
    },
}

# Título e introdução
st.title("Sistema de Legislação de Infrações")
area = st.number_input("Área (m²):", min_value=0, step=1)
st.markdown("Selecione a situação e a ação para obter a legislação aplicável.")

# Opções para selecionar a situação
situacao = st.selectbox("Escolha a situação", list(situacoes.keys()))

# Exibição dos motivos fiscais da situação escolhida
motivos_fiscais = situacoes[situacao]['Motivo Fiscal']
motivo = st.selectbox("Escolha o motivo fiscal", list(motivos_fiscais.keys()))

# Opções para a ação (usando botão de opção)
acao = st.radio("Escolha a ação", [
    "Auto de Notificação",
    "Auto de Embargo",
    "Intimação Demolitória",
    "Auto de Apreensão",
    "Interdição",
    "Auto de Infração"
])

# Função para calcular o valor de k baseado na área
def calcular_k(area):
    if area <= 500:
        return 1
    elif 500 < area <= 1000:
        return 3
    elif 1000 < area <= 5000:
        return 5
    else:
        return 10

nivel = situacoes[situacao]["nivel"]

valores_nivel = {
    "Leve": 432.51,
    "Média": 1441.73,
    "Grave": 2883.46,
    "Gravíssima": 7208.66
}

# Botão para obter a legislação
if st.button("Obter Legislação"):
    legislacao_infringida, artigos_acao = obter_legislacao(situacao, acao)
    
    # Exibição do resultado
    st.subheader("Motivo Fiscal")
    st.markdown(motivos_fiscais[motivo])

    st.subheader("Legislação Infringida")
    st.markdown(legislacao_infringida)
    
    st.subheader("Artigos da Ação Selecionada")
    st.markdown(artigos_acao)
    
    st.subheader(f"**Nível: {situacoes[situacao]['nivel']}**")
    
    k = calcular_k(area)
    st.markdown(f"Valor de k: {k}")

    st.markdown(f"O valor da multa, sem a multiplicação pelo K, é R$ {valores_nivel[nivel]:,.2f}")

    ValorMulta = k * valores_nivel[nivel]
    st.subheader(f"O valor total da multa é R$ {ValorMulta}")
"""



    
