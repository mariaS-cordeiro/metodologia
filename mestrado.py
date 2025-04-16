import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Ambiente de Metodologia de Pesquisa", layout="wide")

st.title("🔍 Ambiente Interativo de Metodologia de Pesquisa")
st.markdown("Este ambiente foi criado para explorar diferentes abordagens metodológicas de forma prática e interativa.")

aba = st.sidebar.radio("Escolha uma abordagem/metodologia:", [
    "Abordagem Qualitativa",
    "Abordagem Quantitativa",
    "Estudo de Caso",
    "Base de Dados Textuais",
    "Base com Vídeos"
])

# ----------- ABA QUALITATIVA ----------- #
if aba == "Abordagem Qualitativa":
    st.header("🧠 Abordagem Qualitativa")
    uploaded_file = st.file_uploader("Envie um arquivo .txt com uma entrevista ou relato")
    if uploaded_file:
        texto = uploaded_file.read().decode("utf-8")
        st.text_area("Texto da Entrevista:", value=texto, height=300)

        categoria = st.selectbox("Categoria interpretativa", [
            "Argumento central", "Marcas de subjetividade", "Estratégia retórica", "Apelo emocional"
        ])
        anotacao = st.text_area("Sua anotação ou interpretação sobre o trecho")
        if st.button("Salvar anotação"):
            st.success("Anotação salva com sucesso!")

# ----------- ABA QUANTITATIVA ----------- #
elif aba == "Abordagem Quantitativa":
    st.header("📊 Abordagem Quantitativa")
    arquivo_csv = st.file_uploader("Envie uma base de dados (.csv)", type="csv")
    if arquivo_csv:
        df = pd.read_csv(arquivo_csv)
        st.write("Pré-visualização dos dados:", df.head())
        st.write("Estatísticas Descritivas:", df.describe())

        coluna = st.selectbox("Escolha uma coluna numérica para visualizar:", df.select_dtypes(include='number').columns)
        st.line_chart(df[coluna])

# ----------- ABA ESTUDO DE CASO ----------- #
elif aba == "Estudo de Caso":
    st.header("🔍 Estudo de Caso")
    caso = st.selectbox("Escolha um caso para explorar:", [
        "Caso Mariana", "Greve dos Caminhoneiros", "COP 30", "Inundações em Recife"
    ])
    st.text_input("Hipótese ou questão central:")
    st.text_area("Notas de observação e análise:")
    st.markdown("---")
    st.markdown("Use esta seção para desenvolver o raciocínio analítico sobre o caso selecionado.")

# ----------- ABA TEXTUAL ----------- #
elif aba == "Base de Dados Textuais":
    st.header("📄 Análise de Base Textual")
    base_textual = st.file_uploader("Envie uma base de comentários ou textos (.csv com uma coluna de texto)")
    if base_textual:
        df_text = pd.read_csv(base_textual)
        coluna_texto = st.selectbox("Escolha a coluna com os textos:", df_text.columns)
        texto_completo = " ".join(df_text[coluna_texto].astype(str))

        st.subheader("Exibição de Palavras Frequentes")
        palavras = texto_completo.split()
        frequencia = pd.Series(palavras).value_counts().head(20)
        st.bar_chart(frequencia)

# ----------- ABA VÍDEO ----------- #
elif aba == "Base com Vídeos":
    st.header("🎥 Análise de Vídeo")
    st.video("https://www.youtube.com/watch?v=6xSxXiHwMrg")  # Exemplo
    st.slider("Minutagem do vídeo para observação:", 0, 300, 0)
    st.text_area("Anotação sobre este trecho do vídeo")
    if st.button("Salvar anotação do vídeo"):
        st.success("Anotação registrada com sucesso!")
