import streamlit as st
import pandas as pd

# Dados fornecidos
dados = {
    "Ano": [2020, 2021, 2022, 2023, 2024, 2025],
    "Coluna 2": [1.71, 1.8, 2, 2.12, 2.2, 2.31],
    "Coluna 3": [0.23, 0.24, 0.27, 0.29, 0.3, 0.31]
    "Coluna 4": [
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
            resultado = campo1 * row["Coluna 2"] + ((campo1-1000) * row["Coluna 3"])
        resultados.append((row["Ano"], resultado))
        soma_total += resultado


    # Exibe os resultados
    st.subheader("Resultados")
    for ano, resultado in resultados:
        st.write(f"Ano {ano:.0f}: R$ {resultado:.2f}")

else:
    st.warning("Por favor, selecione ao menos um ano.")


    
