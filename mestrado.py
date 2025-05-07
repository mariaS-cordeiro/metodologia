import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

st.set_page_config(page_title="Laboratório de Metodologia", layout="wide")

st.title("🧪 Laboratório de Abordagens - Pesquisa em Comunicação Digital")
st.write("Escolha uma abordagem, carregue sua base e veja o que ela pode te responder!")

# Upload do arquivo CSV
arquivo = st.file_uploader("Carregue sua base de dados (.csv):", type="csv")

# Seleção da abordagem
abordagem = st.radio("Selecione a abordagem de análise:", ["Quantitativa", "Qualitativa", "Mista"])

# Caso o usuário carregue uma base
if arquivo:
    df = pd.read_csv(arquivo)
    st.subheader("Pré-visualização da base de dados")
    st.dataframe(df.head())

    texto_colunas = df.select_dtypes(include=['object']).columns.tolist()

    if abordagem == "Quantitativa":
        st.subheader("🔢 Análise Quantitativa")
        coluna_freq = st.selectbox("Escolha a coluna para analisar frequência de termos: ", texto_colunas)

        freq = df[coluna_freq].value_counts().head(10)
        fig, ax = plt.subplots()
        freq.plot(kind='bar', ax=ax)
        ax.set_title("Top 10 valores mais frequentes")
        st.pyplot(fig)

    elif abordagem == "Qualitativa":
        st.subheader("🗣️ Análise Qualitativa - Nuvem de Palavras")
        coluna_texto = st.selectbox("Escolha a coluna de texto para gerar a nuvem:", texto_colunas)

        texto = " ".join(df[coluna_texto].dropna().astype(str))
        nuvem = WordCloud(width=800, height=400, background_color='white').generate(texto)
        fig, ax = plt.subplots()
        ax.imshow(nuvem, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

    elif abordagem == "Mista":
        st.subheader("🔀 Abordagem Mista: Frequência + Palavra-chave")
        coluna = st.selectbox("Escolha a coluna de texto:", texto_colunas)
        df['palavra_chave'] = df[coluna].str.extract(r'(\b\w{5,}\b)', expand=False)
        st.write("Visualização das palavras-chave (palavras com mais de 5 letras):")
        st.dataframe(df[['palavra_chave']].value_counts().head(10))

        texto = " ".join(df[coluna].dropna().astype(str))
        nuvem = WordCloud(width=800, height=400, background_color='white').generate(texto)
        fig, ax = plt.subplots()
        ax.imshow(nuvem, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

else:
    st.info("⚠️ Carregue um arquivo .csv para começar a análise.")
