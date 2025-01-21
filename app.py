import streamlit as st
import pandas as pd

# Dados fornecidos
dados = {
    "Ano": [2020, 2021, 2022, 2023, 2024, 2025],
    "Coluna 2": [1.71, 1.8, 2, 2.12, 2.2, 2.31],
    "Coluna 3": [0.23, 0.24, 0.27, 0.29, 0.3, 0.31],
    "Coluna 4": [0.15, 0.16, 0.17, 0.18, 0.19, 0.2]
}

df = pd.DataFrame(dados)

# Função para primeira página (calculadora TEO)
def pagina_teo():
    st.title("Taxa de Execução de Obras (TEO)")

    campo1 = st.number_input("Insira a área da construção em m²:", min_value=0.0, step=1.0, format="%.2f")

    if campo1 <= 0:
        st.warning("Insira uma área válida para continuar.")
    else:
        anos_selecionados = []
        st.subheader("Selecione os anos:")
        for ano in df["Ano"]:
            if st.checkbox(str(ano)):
                anos_selecionados.append(ano)

        if anos_selecionados:
            dados_filtrados = df[df["Ano"].isin(anos_selecionados)]
            if dados_filtrados.empty:
                st.warning("Nenhum dado encontrado para os anos selecionados.")
            else:
                resultados = []
                soma_total = 0
                for _, row in dados_filtrados.iterrows():
                    if campo1 <= 1000:
                        resultado = campo1 * row["Coluna 2"]
                    else:
                        resultado = 1000 * row["Coluna 2"] + ((campo1 - 1000) * row["Coluna 3"])
                    resultados.append((row["Ano"], resultado))
                    soma_total += resultado

                st.subheader("Resultados")
                for ano, resultado in resultados:
                    st.write(f"Ano {ano:.0f}: R$ {resultado:.2f}")

        else:
            st.warning("Por favor, selecione ao menos um ano.")

# Função para segunda página (simples link)
def pagina_secundaria():
# Dicionário com os dados das infrações
    infracoes = {
    "Executar obra de habitação unifamiliar sem o acompanhamento e registro profissional": {
        'nome': 'Executar obra de habitação unifamiliar sem o acompanhamento e registro profissional',
        'nivel': 'LEVE',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, I, II, VI, 53-A da Lei nº 6.138/2018.\nArts. 68, VI da Dec nº 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO\nFalta de Anotação de Responsabilidade Técnica',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Ausência de Responsável Técnico em obra de habitação unifamiliar, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §1º, I, 124 I e 125 da Lei nº 6.138/2018.\nArts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Responsável Técnico, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §1º, I, 124 III e 131 da Lei nº 6.138/2018.\nArts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Responsável Técnico, intima-se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §1º, I, 124 V e 133 da Lei nº 6.138/2018.\nArts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por ausência de Responsável Técnico em obra de habitação unifamiliar, apreende-se.',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §1º, I, 124 VI, 134 e 135 da Lei nº 6.138/2018.\nArts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Embargo nºxxxx-xxxxxx-OEU, Ausência de Responsável Técnico.',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §1º, I, 124, II, 126, I, 127, 128 da Lei nº 6.138/2018.\nArts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    "Depositar materiais de construção e equipamentos em área pública, sem autorização": {
        'nome': 'Depositar materiais de construção e equipamentos em área pública, sem autorização',
        'nivel': 'LEVE',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, VII, 85, I, III e IV da Lei nº 6.138/2018.\nArts. 115 da Dec nº 43.056/2022',
        'Assuntos_Casos': 'CANTEIRO DE OBRAS\nFalta de Licença Específica (Canteiro de Obras em área pública);\nDescumprimento de Plano de Gerenciamento de Resíduos da Construção Civil',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Ausência de Licença e/ou autorização para uso de área pública, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §1º, II, 124 I e 125 da Lei nº 6.138/2018.\nArts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Licença e/ou autorização para uso de área pública, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §1º, II, 124 III e 131 da Lei nº 6.138/2018.\nArts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe.',
        'embasamento_intimacao': 'Não cabe.',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por ausência de Licença e/ou autorização para uso de área pública, apreende-se.',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §1º, II,124 VI, 134 e 135 da Lei nº 6.138/2018.\nArts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência ou Embargo nºxxxx-xxxxxx-OEU, Ausência de Licença e/ou autorização para uso de área pública.',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §1º, II, 124, II, 126,  I, 127, 128 da Lei nº 6.138/2018.\nArts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de manter, no canteiro de obras, placa informativa de dados técnicos do projeto e obra': {
        'nome': 'Deixar de manter, no canteiro de obras, placa informativa de dados técnicos do projeto e obra',
        'nivel': 'LEVE',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, IV e XI da Lei nº 6.138/2018. Arts. 108 e 163 da Dec nº 43.056/2022',
        'Assuntos_Casos': 'CANTEIRO DE OBRAS, Falta de Placa Informativa fixada em local visível; Placa informativa sem todos os dados da obra e de Responsáveis Técnicos',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Ausência de Placa Informativa. notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §1º, III, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Placa Informativa, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §1º, III, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, Ausência de Placa Informativa',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §1º, III, 124, II, 126, I, 127, 128 da Lei nº 6.138/2018 Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de comunicar à fiscalização a paralisação da obra': {
        'nome': 'Deixar de comunicar à fiscalização a paralisação da obra',
        'nivel': 'LEVE',
        'Infratores': 'Responsável Técnico',
        'legislacao_infringida': 'Arts. 18, IV da Lei nº 6.138/2018. Arts. 11, § 2º da Dec nº 43.056/2022',
        'Assuntos_Casos': 'FISCALIZAÇÂO; Obra licenciada paralisada sem comunicação ao DF-Legal;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Paralisação de obra não comunicada ao órgão de fiscalização, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §1º, IV, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Paralisação de obra não comunicada ao órgão de fiscalização, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §1º, IV, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por paralisação de obra não comunicada ao órgão de fiscalização apreende-se',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §1º, IV, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, Paralisação de obra não comunicada ao órgão de fiscalização',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §1º, IV,  124, II, 126, I, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Descumprir os termos do licenciamento de canteiro de obras e estandes de vendas': {
        'nome': 'Descumprir os termos do licenciamento de canteiro de obras e estandes de vendas',
        'nivel': 'LEVE',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, III, 51, 54, I, IV, 59, 67, §4º, 71 I, IV, 78, 79 e 81 da Lei nº 6.138/2018. Arts. 69, 70, 71, 90, 109, 111 a 114 e 118 a 120 da Dec nº 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO E CANTEIRO DE OBRAS. Descumprimento do Alvará de Construção; Descumprimento da Licença Específica;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Descumprimento de licença de canteiro e/ou estande de venda, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §1º, V, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Descumprimento de licença de canteiro e/ou estande de venda, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §1º, V, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Descumprimento de licença de canteiro e/ou estande de venda, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §1º, I, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por descumprimento de licença de canteiro e/ou estande de venda, apreende-se',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §1º, V, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, Descumprimento de licença de canteiro e/ou estande de venda',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §1º, V, 124, II, 126, I, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Executar obras ou manter edificações passíveis de regularização, localizadas em área privada, sem licença ou em desacordo com o projeto habilitado;': {
        'nome': 'Executar obras ou manter edificações passíveis de regularização, localizadas em área privada, sem licença ou em desacordo com o projeto habilitado;',
        'nivel': 'MÉDIA',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 14, 15, III, 20, 22 e 50 da Lei nº 6.138/2018. Arts. 77 a 84 do Dec nº 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO. Falta de Alvará de Construção; Obra em desacordo com Projeto Habilitado;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Ausência de Licença para obras ou obra em desacordo com projeto habilitado, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, I, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Licença para obras ou obra em desacordo com projeto habilitado, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, I, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por ausência de Licença para obras ou obra em desacordo com projeto habilitado, apreende-se',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §2º, I, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, Ausência de Licença para obras ou obra em desacordo com projeto habilitado',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §2º, I, 124, II, 126 - II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Causar impedimento ou embaraço à atividade de fiscalização;': {
        'nome': 'Causar impedimento ou embaraço à atividade de fiscalização;',
        'nivel': 'MÉDIA',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, V  da Lei nº 6.138/2018-',
        'Assuntos_Casos': 'FISCALIZAÇÂO DESVIO DE CONDUTA. Impedimento à boa e correta fiscalização que inclui: Dificultar acesso interno a obra; Dificultar acesso a documentos necessários de licenças, autorizações e responsabilidade técnica obrigatórios; Dificultar o registro fotográfico e outros necessários à vistoria ou auditoria; Constrangimento ao Auditor em sua atividade, seja por presença física ou atitude de aspecto moral; Não responder ao chamado ',
        'nec_adver_notifca': 'NÃO',
        'detalhamento_advertencia': 'Por Dificultar a atividade de fiscalização, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, II, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Dificultar a atividade de fiscalização, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, II, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por dificultar a atividade de fiscalização, apreende-se',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §2º, II, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Dificultar a atividade de fiscalização',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §2º, II, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Manter obra ou edificação abandonada;': {
        'nome': 'Manter obra ou edificação abandonada;',
        'nivel': 'MÉDIA',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, VII, XIII, 23, XI, 114 da Lei nº 6.138/2018.',
        'Assuntos_Casos': 'FISCALIZAÇÂO. Obra ou edificação abandonada sem atendimentos aos requisitos de manutenção para estanquidade estrutural e segurança; Manter limpo e com os devidos cuidados sanitários',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Falta de manutenção de obra ou edifício (abandono), notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, III, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Não cabe',
        'embasamento_embargo': 'Não cabe',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por falta de manutenção de obra ou edifício abandonado, apreende-se',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §2º, III, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU.  Falta de manutenção de obra ou edifício (abandono)',
        'infracao_embasamento': 'Arts. 13, I, X, 117,122, 123, §2º, III, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de reparar os danos causados na pavimentação ou na urbanização;': {
        'nome': 'Deixar de reparar os danos causados na pavimentação ou na urbanização;',
        'nivel': 'MÉDIA',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts. 15, VII, VIII. X, 18, III, da Lei nº 6.138/2018.',
        'Assuntos_Casos': 'DANOS AO PATRIMÔNIO PÚBLICO. Pavimentação inclui: Calçadas, ciclovias, canteiros de vias e vias públicas danificadas por passagem de equipamentos de obras ou por intervenção não licenciada; Urbanização inclui: Jardins, praças, quadras, áreas de lazer e desporto, parques públicos danificados por passagem de equipamentos de obras ou por intervenção não licenciada',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Falta de reparos aos danos causados na pavimentação e espaços urbanizados, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, IV, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Falta de reparos aos danos causados na pavimentação e espaços urbanizados, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, IV, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Falta de reparos aos danos causados na pavimentação e espaços urbanizados',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §2º, IV, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de alterar os documentos de licenciamento, no caso de transferência de propriedade ou alteração do responsável técnico;': {
        'nome': 'Deixar de alterar os documentos de licenciamento, no caso de transferência de propriedade ou alteração do responsável técnico;',
        'nivel': 'MÉDIA',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts 14, 15, I. XI, XIII da Lei nº 6.138/2018. Arts 68 do Dec 43.056/2022;',
        'Assuntos_Casos': 'LICENCIAMENTO. Atualização de documentos, licenças e autorizações;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Necessidade de alteração de documentos de licenciamento para adequação de proprietário e/ou responsável técnico, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, V, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado pela Necessidade de alteração de documentos de licenciamento para adequação de proprietário e/ou responsável técnico, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, V, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Necessidade de alteração de documentos de licenciamento para adequação de proprietário e/ou responsável técnico',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §2º, V, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de apresentar, quando solicitado pela fiscalização, a documentação de licenciamento;': {
        'nome': 'Deixar de apresentar, quando solicitado pela fiscalização, a documentação de licenciamento;',
        'nivel': 'MÉDIA',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, III, V, VI, 18, VII, 22 da Lei nº 6.138/2018. Arts. 68 do Dec 43.056/2022;',
        'Assuntos_Casos': 'FISCALIZAÇÂO. Impedimento à boa e correta fiscalização;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Documentação de licenciamento não apresentada à autoridade fiscal, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, VI, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Documentação de licenciamento não apresentada à autoridade fiscal, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, VI, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Documentação de licenciamento não apresentada à autoridade fiscal, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §1º, I, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V e 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por documentação de licenciamento não apresentada à autoridade fiscal, apreende-se',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §2º, VI, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Documentação de licenciamento não apresentada à autoridade fiscal',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123 §2º, VI, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de garantir a acessibilidade à área pública no entorno da projeção ou do lote, durante a execução da obra;': {
        'nome': 'Deixar de garantir a acessibilidade à área pública no entorno da projeção ou do lote, durante a execução da obra;',
        'nivel': 'MÉDIA',
        'Infratores': 'Solidária:Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, VIII, 18,  I. II e III da Lei nº 6.138/2018. Arts. 68, IX, b, 119, 120, do Dec. 43.056/2022;',
        'Assuntos_Casos': 'ACESSIBILIDADE. Calçamento obstruído com container, tapumes ou outros equipamentos da obra',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Acessibilidade comprometida em área pública lindeira ao imóvel, na fase da obra, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, VII, 124 I, e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I,169,170 e171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado pela Acessibilidade comprometida em área pública lindeira ao imóvel, na fase da obra, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, VII, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Acessibilidade comprometida em área pública lindeira ao imóvel, na fase da obra, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §2º, VII, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de garantir a acessibilidade à área pública no entorno da projeção ou do lote, durante a execução da obra, apreende-se',
        'embasamento_apreensao': '----',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Acessibilidade comprometida em área pública lindeira ao imóvel, na fase da obra',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §2º, VII, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de observar o correto direcionamento das águas pluviais para a rede pública.': {
        'nome': 'Deixar de observar o correto direcionamento das águas pluviais para a rede pública.',
        'nivel': 'MÉDIA',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts. 15, VII, VIII, 18, I, II, VI, 79, § 2º, 82, 84 da Lei nº 6.138/2018',
        'Assuntos_Casos': 'DANOS AO PATRIMÔNIO PÚBLICO. Águas pluviais destinadas diretamente nas vias ou logradouros públicos (sem sistema); Falta de manutenção no sistema de coleta de águas pluviais da obra ou edificação afetando as vias ou logradouros públicos (com sistema)',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Corrigir o escoamento de águas pluviais à rede pública, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §2º, VIII, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado pela necessidade de Correção do escoamento de águas pluviais à rede pública, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §2º, VIII, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': '',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §2º, VIII, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §2º, VIII, 124, II, 126, II, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Executar obras ou manter edificações passíveis de regularização, localizadas em área pública, sem licença ou em desacordo com o projeto habilitado': {
        'nome': 'Executar obras ou manter edificações passíveis de regularização, localizadas em área pública, sem licença ou em desacordo com o projeto habilitado',
        'nivel': 'GRAVE',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts 18, V, 54, 58, 71 da Lei nº 6.138/2018. Arts 29, III, IV, 47 do Dec. 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO. Obras de urbanização não previstas no licenciamento (cercamento, calçamento, ajardinamento, rebaixamento de vias e outras intervenções); Instalação de coberturas, pequenas centrais elétricas térreas ou subterrâneas, pequenas edificações provisórias  complementares às atividades de obra não previstas ou em dela',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Providenciar regularização de obras e/ou edificação em área pública (sem licença ou em desacordo com projeto habilitado), notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, I,124 I e 125 da Lei nº 6.138/2018. Arts 167, 168 I, 169,170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Providenciar regularização de obras e/ou edificação em área pública (sem licença ou em desacordo com projeto habilitado), embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, I,124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar regularização de obras e/ou edificação em área pública (sem licença ou em desacordo com projeto habilitado',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, I,124 III e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar regularização de obras e/ou edificação em área pública (sem licença ou em desacordo com projeto habilitado',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §3º, I,124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Embargo nºxxxx-xxxxxx-OEU. Descumprimento de Intimação Demolitória nºxxxx-xxxxxx-OEU',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, I, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Executar obras ou manter edificações não passíveis de regularização em área privada': {
        'nome': 'Executar obras ou manter edificações não passíveis de regularização em área privada',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/ Responsável Técnico',
        'legislacao_infringida': 'Arts 15 II, III, 18, V, VII, 22 da Lei nº 6.138/2018',
        'Assuntos_Casos': 'LICENCIAMENTO. Obra em lote não regularizado; Obras em desrespeito aos Parâmetros Urbanísticos; Obras em área de proteção ambiental dentro de lotes privados;',
        'nec_adver_notifca': 'NÃO',
        'detalhamento_advertencia': 'Não cabe',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, II, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Por ser obra e/ou edificação não passível de regularização, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, II, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Obra e/ou edificação não passível de regularização, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, II, 124, V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, Obra e/ou edificação não passível de regularização, em atenção aos Arts 134 e 135 da Lei nº 6.138/2018 e Art. 182 do Dec. nº 43.056/2022',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §3º, II, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Embargo nºxxxx-xxxxxx-OEU. Descumprimento de Intimação Demolitória nºxxxx-xxxxxx-OEU',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, II, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de reparar os danos causados às redes de infraestrutura pública durante a obra': {
        'nome': 'Deixar de reparar os danos causados às redes de infraestrutura pública durante a obra',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts. 15, VII, VIII, X, 18, III da Lei nº 6.138/2018.',
        'Assuntos_Casos': 'DANOS AO PATRIMÔNIO PÚBLICO. Rompimento ou dano a: a rede de abastecimento de água ou a Estações de bombeamento;  A rede elétrica, postes, transmissores e outros equipamentos públicos como subestações de energia a rede pluvial, galerias, bocas de lobo, bacias de contenção e outros elementos, A rede de esgotamento, caixas de passagem,  estações de bombeamento, fossas e outros elementos;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Providenciar a reparação de redes de infraestrutura por danos causados durante obra, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, III, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Providenciar a reparação de redes de infraestrutura por danos causados durante obra, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, III, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar a reparação de redes de infraestrutura por danos causados durante obra',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, III, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Negligenciar a conservação e a segurança da obra ou da edificação': {
        'nome': 'Negligenciar a conservação e a segurança da obra ou da edificação',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, 18, I, II, III da Lei nº 6.138/2018.',
        'Assuntos_Casos': 'MANUTENÇÃO, CONSERVAÇÃO E SEGURANÇA. Situações de Risco de: Acidente: fator que coloque o trabalhador em situação vulnerável e possa afetar sua integridade. as máquinas e equipamentos sem proteção, probalidade de desabamento ou colapso estrutural, probabilidade de incêndio e explosão, arranjo físico inadequado, armazenamento inadequado, etc; Ergonômico: diversas formas de energia a que possam estar expostos os trabalhadores, tais como: ruído, calor, frio, pressão, umidade, radiações ionizantes e não-ionizantes, vibração, etc Químico:substâncias, compostos ou produtos que possam penetrar no organismo do trabalhador pela via respiratória, nas formas de poeiras, fumos gases, neblinas, névoas ou vapores; Falta de conservação de estrutura, vedações, coberturas ou elementos da obra ou edificação em desrespeito a Plano de Conservação ou a boa prática de obras;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Providenciar a conservação e segurança da obra e edificações, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, IV, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Providenciar a conservação e segurança da obra e edificações, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, IV, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Providenciar a conservação e segurança da obra e edificações, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §2º, VII, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar a conservação e segurança da obra e edificações',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, IV, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de garantir a estabilidade do solo no canteiro de obras': {
        'nome': 'Deixar de garantir a estabilidade do solo no canteiro de obras',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/ Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, 18, III, IX da Lei nº 6.138/2018.',
        'Assuntos_Casos': 'MANUTENÇÃO, CONSERVAÇÃO E SEGURANÇA. Falta de cuidados na contenção de taludes, escavações ou aterros; Compactação incorreta de solo; Excesso de impermeabilização ou outras alterações do solo natural sem o devido acompanhamento técnico;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por deixar de garantir a estabilidade do solo no canteiro de obras, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, V, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167,168 I, 169, 170 e 171  do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Garantir a estabilidade do solo no canteiro de obras, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, V, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Garantir a estabilidade do solo no canteiro de obras, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, V, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Garantir a estabilidade do solo no canteiro de obras',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, V, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Colocar em risco a estabilidade e a integridade das propriedades vizinhas e das áreas públicas': {
        'nome': 'Colocar em risco a estabilidade e a integridade das propriedades vizinhas e das áreas públicas',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, 18. I, II, III da Lei nº 6.138/2018.',
        'Assuntos_Casos': 'MANUTENÇÃO, CONSERVAÇÃO E SEGURANÇA; Escavações nas divisas ou próximas a elas sem os devidos cuidados, estruturas ou estudos de estabilidade do solo provocando movimentação de solo com dano ao patrimônio público e privado; Execução de muros de divisa convencionais ou outros, como arrimo, sem cuidados de execução e limpeza; Edificação próximas as divisas ou em altura, que possa ocasionar queda de material, ferramentas ou outros elementos no terreno vizinho sem as devidas cortinas de proteção e outros elementos;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por colocar em risco a estabilidade e integridade das propriedades privadas e áreas públicas, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por colocar em risco a estabilidade e integridade das propriedades privadas e áreas públicas, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por colocar em risco a estabilidade e integridade das propriedades privadas e áreas públicas, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Garantir a estabilidade e integridade das propriedades privadas e áreas públicas',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de desocupar ou recuperar a área pública após o término da obra': {
        'nome': 'Deixar de desocupar ou recuperar a área pública após o término da obra',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, VIII, 18, I, II, III, V, 81 da Lei nº 6.138/2018. Arts 68, VII, 70, § 3º, 71, VII do Dec. 43.056/2022',
        'Assuntos_Casos': 'MANUTENÇÃO, CONSERVAÇÃO E SEGURANÇA. Restos de materiais depositados nas áreas públicas ou rejeitos da construção; Não reparação de calçadas, vias, ciclovias, ajardinamentos nas áreas que sofreram danos pela movimentação de equipamentos ou por utilização de espaço; Não reparação de redes públicas alteradas ou danificadas durante a obra, que não estavam inseridos nos cuidados impostos para intervenção em áreas públicas;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Deixar de desocupar e recuperar a área pública após o término da obra, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, VII, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Desocupar e recuperar a área pública após o término da obra, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, VII, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Desocupar e recuperar a área pública após o término da obra, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Desocupar e recuperar a área pública após o término da obra',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de providenciar os cuidados obrigatórios impostos para a intervenção em áreas públicas': {
        'nome': 'Deixar de providenciar os cuidados obrigatórios impostos para a intervenção em áreas públicas',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 18, I, III, V, 58 da Lei nº 6.138/2018. Arts 68, VII, 70, §3º, 71, VII, 87, III, IV do Dec 43.056/2022',
        'Assuntos_Casos': 'MANUTENÇÃO, CONSERVAÇÃO E SEGURANÇA. Atender as exigências do Alvará de Construção e ou da Licença Especial quanto a reparação, adequação e ou reforma das áreas públicas;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Deixar de Providenciar os cuidados obrigatórios impostos para a intervenção em áreas públicas, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, VIII, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I,169,170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Providenciar os cuidados obrigatórios impostos para a intervenção em áreas públicas, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, VIII, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Providenciar os cuidados obrigatórios impostos para a intervenção em áreas públicas, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': '',
        'embasamento_apreensao': '',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar os cuidados obrigatórios impostos para a intervenção em áreas públicas',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de respeitar o Plano de Gerenciamento de Resíduos da Construção Civil': {
        'nome': 'Deixar de respeitar o Plano de Gerenciamento de Resíduos da Construção Civil',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, XVI, 18, I, V, VI da Lei nº 6.138/2018. Arts 68, §1º do Dec. 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO E CANTEIRO DE OBRAS. Observação existência de containers para a deposição de resíduos da construção; Descarte adequado de terras e outros materiais gerados na escavação em local adequado e devidamente autorizado; Correta separação de materiais e rejeitos da obra;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por desrespeitar o Plano de Gerenciamento de Resíduos da Construção Civil, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, IX, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 161, V, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por desrespeitar o Plano de Gerenciamento de Resíduos da Construção Civil, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, IX, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Respeitar o Plano de Gerenciamento de Resíduos da Construção Civil',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 161, V, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Poluir ou assorear cursos de água e sistemas de drenagem públicos': {
        'nome': 'Poluir ou assorear cursos de água e sistemas de drenagem públicos',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, XVI, 18,  I, II, VI, X, 79, § 2º, 84 da Lei nº 6.138/2018. Arts 29, 70, §1º, VII, § 2º, 112 do Dec. 43.056/2022',
        'Assuntos_Casos': 'DANOS AO PATRIMÔNIO PÚBLICO. Escorrimento de Materiais nas vias públicas; Cuidados para contenção de solo e resíduos da construção diretamente a cursos d’água mesmo dentro da propriedade; Cuidados na retirada de vegetação e outras condições ambientais que sejam barreiras naturais a escorrimento de águas pluviais e solo;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Poluir ou assorear cursos d´Água e sistema de drenagem público, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, X, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Poluir ou assorear cursos d´Água e sistema de drenagem público, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, X, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Poluir ou assorear cursos d´Água e sistema de drenagem público',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Erodir logradouros e terrenos vizinhos por falta de rede de drenagem no canteiro de obras': {
        'nome': 'Erodir logradouros e terrenos vizinhos por falta de rede de drenagem no canteiro de obras',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária:Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, XVI, 18, I, II, III, 79, §§2º, 3º, 82, I, 84, da Lei nº 6.138/2018. Arts 29, 68, VII, 70, §1º, VII, §3º, 112 do Dec. 43.056/2022',
        'Assuntos_Casos': 'CONSERVAÇÃO E SEGURANÇA. Por falta de rede pluvial no canteiro de obras, há perda de solo e danos ao patrimônio privado e ou público;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Contenção erosão de logradouros e propriedade propriedades vizinhas por conta de drenagem no canteiro de obras',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123 §3º, XI, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I,169,170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Contenção erosão de logradouros e propriedade propriedades vizinhas por conta de drenagem no canteiro de obras',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123 §3º, XI, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Contenção erosão de logradouros e propriedade propriedades vizinhas por conta de drenagem no canteiro de obras',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123 §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de garantir a acessibilidade universal em todos os acessos à edificação': {
        'nome': 'Deixar de garantir a acessibilidade universal em todos os acessos à edificação',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, VIII, XVI, 18, III, 55, II, 62, §§ 1º, 3º, 4º, 63, I, 67, §3º, I, 79, § 3º, II, 85, §2º, 86, II, 87, 88, 89, 90 da Lei nº 6.138/2018. Arts 33, 70, §1º, II, 74, §3º, 75, §3º, 87, V, VI, VII, 105, II, 106, 112, 123, 124, 125 do Dec. 43.056/2022',
        'Assuntos_Casos': 'ACESSIBILIDADE. Falta ou dimensões inadequadas de rampas, calçadas, elevadores ou escadas que permitam o acesso de pessoas e veículos respeitadas a NBR9050 e Decreto 38.047/2017;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Necessidade de garantia de acessibilidade universal em todos os acessos à edificação',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, XII, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de garantir de acessibilidade universal em todos os acessos à edificação, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, XII, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de garantir a acessibilidade universal em todos os acessos à edificação, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §3º, XII, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Necessidade de garantia de acessibilidade universal em todos os acessos à edificação',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar que materiais de construção e resíduos provenientes de escavação ou movimentação de terra escorram para logradouros públicos ou rede de infraestrutura.': {
        'nome': 'Deixar que materiais de construção e resíduos provenientes de escavação ou movimentação de terra escorram para logradouros públicos ou rede de infraestrutura.',
        'nivel': 'GRAVE',
        'Infratores': 'Solidária:Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, XVI, 18, VI, VII, IX, X, 79, §2º, 83, 84, 95, da Lei nº 6.138/2018. Arts 68 §1º, 115 do Dec 43.056/2022.',
        'Assuntos_Casos': 'DANOS AO PATRIMÔNIO PÚBLICO.',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Evitar que materiais de construção e resíduos de escavação ou movimentação de terra escorram para logradouros públicos ou rede de infraestrutura.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §3º, XIII, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar que materiais de construção e resíduos de escavação ou movimentação de terra escorram para logradouros públicos ou rede de infraestrutura, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §3º, XIII, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Evitar que materiais de construção e resíduos de escavação ou movimentação de terra escorram para logradouros públicos ou rede de infraestrutura.',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §3º, VI, 124, II, 126, III, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de adotar as providências determinadas pelo órgão competente em obras e edificações com risco iminente ou abandonada;': {
        'nome': 'Deixar de adotar as providências determinadas pelo órgão competente em obras e edificações com risco iminente ou abandonada;',
        'nivel': 'GRAVÍSSIMA',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15, VII, X, 18, I, II, III, da Lei nº 6.138/2018. Arts 72, 166 do Dec. 43.056/2022',
        'Assuntos_Casos': 'FISCALIZAÇÃO. Pedido de providências, como Laudo de Estanquidade Estrutural, correção de telas e cortinas de segurança em fachadas, andaimes e outras situações em obras com risco detectados: Acidente: fator que coloque o trabalhador em situação vulnerável e possa afetar sua integridade. as máquinas e equipamentos sem proteção, probalidade de desabamento ou colapso estrutural, probabilidade de incêndio e explosão, arranjo físico inadequado, armazenamento inadequado, etc; Ergonômico: diversas formas de energia a que possam estar expostos os trabalhadores, tais como: ruído, calor, frio, pressão, umidade, radiações ionizantes e não-ionizantes, vibração, etc Químico:substâncias, compostos ou produtos que possam penetrar no organismo do trabalhador pela via respiratória, nas formas de poeiras, fumos gases, neblinas, névoas ou vapores; Correção de canteiro de obras ou de rotinas de serviço com mudanças necessárias no Alvará de Construção ou Licença específica;',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Deixar de adotar providências prescritas para conter risco iminente em obras e edificações, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §4º, I, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, por deixar de Adotar providências prescritas para conter risco iminente em obras e edificações, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §4º, I,124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022 ',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por deixar de Adotar providências prescritas para conter risco iminente em obras e edificações, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §4º, I, 124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Não cabe',
        'embasamento_apreensao': 'Não cabe',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Adotar providências prescritas para conter risco iminente em obras e edificações',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §4º, I, 124, II, 126, IV, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168-II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Executar obras ou manter edificações não passíveis de regularização, localizadas em área pública;': {
        'nome': 'Executar obras ou manter edificações não passíveis de regularização, localizadas em área pública;',
        'nivel': 'GRAVÍSSIMA',
        'Infratores': 'Solidária:Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 14, 15, II, IV, VI, 18, V, VII, 22, 50, 52, 54, 55, 151 da Lei nº 6.138/2018. Arts 67, 69, 70, 71, 74, 77 do Dec. 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO. Obra irregular; Edifício irregular; Parcelamento Irregular (grilagem);',
        'nec_adver_notifca': 'NÃO',
        'detalhamento_advertencia': 'Não cabe',
        'embasamento_advertencia': 'Não cabe',
        'detalhamento_embargo': 'Executar obras ou manter edificações não passíveis de regularização, localizadas em área pública, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §4º, II, 124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022',
        'detalhamento_intimacao': 'Executar obras ou manter edificações não passíveis de regularização, localizadas em área pública, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §4º, II,  124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto de Embargo nºxxxx-xxxxxx-OEU. Executar obras ou manter edificações não passíveis de regularização, localizadas em área pública;',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §4º, II, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Embargo nºxxxx-xxxxxx-OEU. Descumprimento de Intimação Demolitória nºxxxx-xxxxxx-OEU. Executar obras ou manter edificações não passíveis de regularização, localizadas em área pública;',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §4º, II, 124, II, 126, IV, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Executar obra sem acompanhamento e registro do profissional habilitado, exceto em habitações unifamiliares;': {
        'nome': 'Executar obra sem acompanhamento e registro do profissional habilitado, exceto em habitações unifamiliares;',
        'nivel': 'GRAVÍSSIMA',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts. 15, I, II, VI, 22, 50, 52 da Lei nº 6.138/2018. Arts. 68, VI, da Dec nº 43.056/2018',
        'Assuntos_Casos': 'LICENCIAMENTO. Falta de Anotação de Responsabilidade Tecnica; Inclui-se Parcelamento Irregular do solo que também requer ART, em conjunto com a Infração nº 15 - Executar obras ou manter edificações não passíveis de regularização em área privada (Art. 123 §3º inciso II)',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por Ausência de Responsável Técnico, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §4º, III, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Responsável Técnico, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §4º, III,124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022 ',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Ausência de Responsável Técnico, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §4º, III,  124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Ausência de Responsável Técnico, exceto habitação familiar',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §4º, III,124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Ausência de Responsável Técnico, exceto habitação familiar',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §4º, III, 124, II, 126, IV, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Descumprir auto de embargo, intimação demolitória e interdição;': {
        'nome': 'Descumprir auto de embargo, intimação demolitória e interdição;',
        'nivel': 'GRAVÍSSIMA',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 15 III, V, 18, I, II, 124, 131, 132, 133 da Lei nº 6.138/2018. Arts 177, 178, 179, 180 do Dec. 43.056/2022',
        'Assuntos_Casos': 'FISCALIZAÇÃO',
        'nec_adver_notifca': 'NÃO',
        'detalhamento_advertencia': 'Não cabe',
        'embasamento_advertencia': 'Não cabe',
        'detalhamento_embargo': 'Não cabe',
        'embasamento_embargo': 'Não cabe',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Descumprimento de auto de embargo, intimação demolitória e interdição;',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §4º, IV,124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022 ',
        'infracao_detalhamento': 'Descumprimento de Auto Embargo nºxxxx-xxxxxx-OEU. Descumprimento de Intimação Demolitória nºxxxx-xxxxxx-OEU',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §4º, IV, 124, II, 126, IV, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Apresentar documentos sabidamente falsos;': {
        'nome': 'Apresentar documentos sabidamente falsos;',
        'nivel': 'GRAVÍSSIMA',
        'Infratores': 'Proprietário',
        'legislacao_infringida': 'Arts 15, I da Lei nº 6.138/2018. Arts 66, IV, §7º do Dec. Nº 43.056/2022',
        'Assuntos_Casos': 'DESVIO DE CONDUTA',
        'nec_adver_notifca': 'NÃO',
        'detalhamento_advertencia': 'Por Documentos sabidamente falsos, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §4º, V, 124 I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Documentos sabidamente falsos, embarga-se e requisita-se a regularização no prazo determinado sob pena de multa.',
        'embasamento_embargo': 'Arts. 13, X, 117, 122, 123, §4º, V,124 III e 131 da Lei nº 6.138/2018. Arts 10, 167, 168 III e 177 do Dec. 43.056/2022 ',
        'detalhamento_intimacao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU, dado por Documentos sabidamente falsos, intima~se a Demolir no prazo determinado sob pena de multa.',
        'embasamento_intimacao': 'Arts. 13, X, 117, 122, 123, §4º, V,  124 V e 133 da Lei nº 6.138/2018. Arts 10, 167, 168 V, 180 e 181 do Dec. 43.056/2022',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Documentos sabidamente falsos',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §4º, I,124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Documentos sabidamente falsos',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §4º, I, 124, II, 126, IV, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    'Deixar de providenciar o atestado de conclusão da obra.': {
        'nome': 'Deixar de providenciar o atestado de conclusão da obra.',
        'nivel': 'GRAVÍSSIMA',
        'Infratores': 'Solidária: Proprietário/Responsável Técnico',
        'legislacao_infringida': 'Arts 14, §1º, 15, XIV, 18, I, II, 61, 62, 67 da Lei nº 6.138/2018. Arts 89, 90, 91, 92, 93, 94, 95 do Dec. 43.056/2022',
        'Assuntos_Casos': 'LICENCIAMENTO',
        'nec_adver_notifca': 'SIM',
        'detalhamento_advertencia': 'Por deixa de providenciar o Atestado de Conclusão de Obras, notifica-se e requisita-se a regularização no prazo determinado sob pena de prosseguimento de ações fiscais.',
        'embasamento_advertencia': 'Arts. 13, X, 117, 122, 123, §4º, VI, 124I e 125 da Lei nº 6.138/2018. Arts 10, 167, 168 I, 169, 170 e 171 do Dec. 43.056/2022',
        'detalhamento_embargo': 'Não cabe',
        'embasamento_embargo': 'Não cabe',
        'detalhamento_intimacao': 'Não cabe',
        'embasamento_intimacao': 'Não cabe',
        'detalhamento_apreensao': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar o Atestado de Conclusão de Obras',
        'embasamento_apreensao': 'Arts. 13, X, 117, 122, 123, §4º, I, 124 VI, 134 e 135 da Lei nº 6.138/2018. Arts 10, 167, 168 VI e 182 do Dec. 43.056/2022',
        'infracao_detalhamento': 'Descumprimento de Auto Advertência nºxxxx-xxxxxx-OEU. Providenciar o Atestado de Conclusão de Obras',
        'infracao_embasamento': 'Arts. 13, X, 117, 122, 123, §4º, I, 124, II, 126, IV, 127, 128 da Lei nº 6.138/2018. Arts 10, 167, 168, II, 172, 173, 174, 175, 176 do Dec. 43.056/2022',
    },
    }
    
    # Interface do aplicativo
    st.title("Sistema de Infrações")
    
    # Interface do aplicativo
    st.title("Sistema de Infrações")
    
    # Entrada de dados do usuário
    area = st.number_input("Área (m²):", min_value=0.0, format="%.2f")
    
    # Seleção de infração
    nome_infracao = st.selectbox("Selecione a infração:", options=list(infracoes.keys()))
    
    # Seleção de ação
    acao = st.radio("Escolha a ação:", [
        "Auto de Notificação",
        "Auto de Embargo",
        "Intimação Demolitória",
        "Auto de Apreensão",
        "Auto de Infração"
    ])
    
    # Seleção múltipla: Fase da Obra
    fases_obra = st.multiselect(
        "Fase da Obra - Serviços Iniciados:",
        options=[
            "Movimentação de terras",
            "Fundações",
            "Alvenarias",
            "Concretagem de lajes",
            "Instalações",
            "Revestimentos",
            "Cobertura",
            "Acabamento"
        ]
    )
    
    # Variável para armazenar o conteúdo a ser copiado
    resultado_copy = ""
    
    # Botão para exibir o resultado
    if st.button("Exibir Resultado"):
        infracao = infracoes[nome_infracao]
    
        # Informações gerais
        resultado_copy += f"Nome: {infracao['nome']}\n"
        resultado_copy += f"Nível: {infracao['nivel']}\n"
        resultado_copy += f"Infratores: {infracao['Infratores']}\n"
        resultado_copy += f"Legislação Infringida: {infracao['legislacao_infringida']}\n"
        resultado_copy += f"Assuntos/Casos: {infracao['Assuntos_Casos']}\n"
        resultado_copy += f"Necessária Advertência/Notificação: {infracao['nec_adver_notifca']}\n"
    
        # Exibição das fases selecionadas
        resultado_copy += "\nFase da Obra - Serviços Iniciados: "
        if fases_obra:
            resultado_copy += ", ".join(fases_obra)
        else:
            resultado_copy += "Nenhuma fase selecionada."
    
        # Detalhamento por ação
        if acao == "Auto de Notificação":
            resultado_copy += f"\nDetalhamento: {infracao['detalhamento_advertencia']}\n"
            resultado_copy += f"Embasamento: {infracao['embasamento_advertencia']}\n"
        elif acao == "Auto de Embargo":
            resultado_copy += f"\nDetalhamento: {infracao['detalhamento_embargo']}\n"
            resultado_copy += f"Embasamento: {infracao['embasamento_embargo']}\n"
        elif acao == "Intimação Demolitória":
            resultado_copy += f"\nDetalhamento: {infracao['detalhamento_intimacao']}\n"
            resultado_copy += f"Embasamento: {infracao['embasamento_intimacao']}\n"
        elif acao == "Auto de Apreensão":
            resultado_copy += f"\nDetalhamento: {infracao['detalhamento_apreensao']}\n"
            resultado_copy += f"Embasamento: {infracao['embasamento_apreensao']}\n"
        elif acao == "Auto de Infração":
            resultado_copy += f"\nDetalhamento: {infracao['infracao_detalhamento']}\n"
            resultado_copy += f"Embasamento: {infracao['infracao_embasamento']}\n"
    
        # Salvar o resultado no estado da sessão
        st.session_state["resultado_editado"] = resultado_copy
    
    # Inicializar o campo editável se não estiver no estado da sessão
    if "resultado_editado" not in st.session_state:
        st.session_state["resultado_editado"] = ""
        
    # Exibição do conteúdo para cópia e edição
    resultado_editado = st.text_area(
        "Resultado para editar e copiar",
        st.session_state["resultado_editado"],
        height=300
    )
        
    # Atualizar o estado da sessão ao editar
    st.session_state["resultado_editado"] = resultado_editado
        
    # Botão para baixar o arquivo .txt
    st.download_button(
        label="Salvar como .txt",
        data=st.session_state["resultado_editado"],
        file_name="resultado_infracao.txt",
        mime="text/plain"
    )
    

# Função para terceira página (simples link)
def pagina_habitese():
    # Função para gerar o arquivo .txt
    def gerar_txt(resultados):
        with open("relatorio.txt", "w") as file:
            for key, value in resultados.items():
                file.write(f"{key}: {value}\n")
        return "relatorio.txt"

    # Função para criar as perguntas e salvar as respostas
    def perguntas():
        resultados = {}

        # Pergunta 1
        st.subheader("1. Pagamento da TEO está regular?")
        pagamento_teo = st.radio("Escolha:", ["Aprovado", "Não regular"], key="teo")
        if pagamento_teo == "Não regular":
            # Opções adicionais
            opcoes_teo = st.multiselect("Marque as opções que se aplicam:", [
                "1.1 Não consta lançamento de TEO para este endereço",
                "1.2 Falta pagamento da TEO no período",
                "1.3 A área declarada na TEO é inferior à área licenciada",
                "1.4 Não constam lançamentos de TEO para o CPF/CNPJ do interessado"
            ], key="opcoes_teo")
            resultados["1. Pagamento da TEO"] = f"Não regular: {', '.join(opcoes_teo)}"
        else:
            resultados["1. Pagamento da TEO"] = "Aprovado"

        # Pergunta 2
        st.subheader("2. O canteiro de obras e o entulho foram retirados de dentro do lote?")
        canteiro_obras = st.radio("Escolha:", ["Aprovado", "Não regular"], key="canteiro_obras")
        if canteiro_obras == "Não regular":
            # Opções adicionais
            opcoes_canteiro = st.multiselect("Marque as opções que se aplicam:", [
                "2.1 O canteiro de obras não foi retirado",
                "2.2 Falta retirar entulhos",
                "2.3 O estande de vendas não foi retirado"
            ], key="opcoes_canteiro")
            resultados["2. Canteiro de obras e entulho"] = f"Não regular: {', '.join(opcoes_canteiro)}"
        else:
            resultados["2. Canteiro de obras e entulho"] = "Aprovado"

        # Caixa de observações
        st.subheader("Observações:")
        observacoes = st.text_area("Escreva suas observações aqui:", key="observacoes")

        if observacoes:
            resultados["Observações"] = observacoes

        return resultados

    # Função principal
    def main():
        st.title("Relatório para habite-se (Em construção)")
        
        resultados = perguntas()

        # Exibe o resumo das respostas
        st.subheader("Resumo das Respostas:")
        for key, value in resultados.items():
            st.write(f"{key}: {value}")
        
        # Botão para gerar o arquivo .txt
        if st.button("Confirmar relatório"):
            file_name = gerar_txt(resultados)
            
            # Fornece o arquivo para download
            with open(file_name, "r") as file:
                st.download_button(
                    label="Baixar TXT",
                    data=file,
                    file_name=file_name,
                    mime="text/plain"
                )

    if __name__ == "__main__":
        main()

def pagina_parametros():
    import pandas as pd

    # Função para procurar o valor no CSV e retornar os valores da linha
    def procurar_valor(df, codigo):
        # Converte o código para string e remove espaços em branco
        codigo = str(codigo).strip()
        
        # Converte a coluna 'lu_cipu' para string e remove espaços em branco
        resultado = df[df['lu_cipu'].astype(str).str.strip() == codigo]  
        
        if not resultado.empty:
            # Retorna o índice da linha e os valores de todas as colunas da linha
            indice = resultado.index[0]  # Índice da linha onde o código foi encontrado
            linha = resultado.iloc[0]  # Valores de todas as colunas dessa linha
            return indice, linha
        else:
            return None, "Código não encontrado"

    # Função para mapear os nomes das colunas para nomes amigáveis
    def mapear_nomes(coluna):
        mapeamento = {
            "lu_cipu": "Código CIPU",
            "lu_end_car": "Endereço Cartorial",
            "lu_ra_luos": "LUOS",
            "lu_uos_par": "UOS Par",
            "st_area_sh": "Área",
            "lu_padrao_": "LUOS",
            "lu_ini_fai": "Inicio de faixa LUOS",
            "lu_fim_fai": "Fim de faixa LUOS",
            "lu_cfa_b": "Aproveitamento básico", 
            "lu_cfa_m": "Aproveitamento máximo",
            "lu_tx_ocu": "Faixa de ocupação",
            "lu_tx_perm": "Taxa de permeabilidade",
            "lu_alt_max": "Altura máxima",
            "lu_afr": "Afastamento frontal", 
            "lu_afu": "Afastamento fundos", 
            "lu_aft_lat": "Afastamento lateral", 
            "llu_aft_l_1": "Afastamento lateral", 
            "lu_aft_obs": "Observação nos afastamentos", 
            "lu_marquis": "Marquise",
            "lu_galeria": "Galeria",
            "lu_cota_so": "Cotas",
            "lu_notas": "Notas",
            "lu_subsol": "Subsolo",
            # Adicione mais mapeamentos conforme necessário
        }
        return mapeamento.get(coluna, None)  # Retorna o nome mapeado ou None se não estiver no mapeamento

    # Função principal
    def main():
        st.title("Busca dos parâmetros através do CIPU")

        # Carregar o arquivo CSV localmente (LUOS.csv) com codificação UTF-8 ou ISO-8859-1
        try:
            df = pd.read_csv('LUOS.csv', encoding='utf-8')  # Tente 'utf-8', ou use 'ISO-8859-1' se houver erro de codificação
            st.write("O código CIPU poderá ser encontrado no SEi")
            
            # Solicitar o código que o usuário deseja procurar
            codigo = st.text_input("Digite o código CIPU", "")

            # Botão para realizar a busca
            if st.button("Buscar") and codigo:
                indice, linha = procurar_valor(df, codigo)
                if indice is not None:

                    # Exibir apenas as colunas que estão no mapeamento
                    for coluna, valor in linha.items():
                        nome_amigavel = mapear_nomes(coluna)
                        if nome_amigavel:  # Só exibe se a coluna estiver no mapeamento
                            st.write(f"{nome_amigavel}: {valor}")
                else:
                    st.write(linha)
        
        except FileNotFoundError:
            st.error("O arquivo LUOS.csv não foi encontrado. Certifique-se de que ele está no mesmo diretório do script.")
        except UnicodeDecodeError:
            st.error("Erro de codificação ao ler o arquivo. Tente utilizar 'ISO-8859-1' ou outra codificação.")

    # Rodar o aplicativo
    if __name__ == "__main__":
        main()


# Lógica de navegação
opcao = st.sidebar.radio("MENU", ("Taxa de Execução de Obras", "Auto Fiscal - COE", "Relatório Habite-se", "Parâmetros Urbanísticos"))

if opcao == "Taxa de Execução de Obras":
    pagina_teo()
elif opcao == "Auto Fiscal - COE":
    pagina_secundaria()
elif opcao == "Parâmetros Urbanísticos":
    pagina_parametros()
else:
    pagina_habitese()
