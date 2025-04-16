import streamlit as st
import pandas as pd
from datetime import datetime
from scipy.stats import ttest_ind, f_oneway

st.set_page_config(page_title="Ambiente de Metodologia de Pesquisa", layout="wide")

st.title("🔍 Ambiente Interativo de Metodologia de Pesquisa")
st.markdown("Este ambiente foi criado para explorar diferentes abordagens metodológicas de forma prática e interativa.")

aba = st.sidebar.radio("Escolha uma abordagem/metodologia:", [
    "Abordagem Qualitativa",
    "Abordagem Quantitativa",
    "Estudo de Caso",
    "Base de Dados Textuais",
    "Base com Vídeos",
    "Simulações Quantitativas"
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

# ----------- ABA SIMULAÇÕES QUANTITATIVAS ----------- #
st.download_button("📥 Baixar base simulada de exemplo", data=open("base_simulada_quantitativa.csv", "rb").read(), file_name="base_exemplo.csv")
elif aba == "Simulações Quantitativas":
    st.header("🧪 Simulações de Pesquisa Quantitativa com Dados Digitais")

    questao = st.selectbox("Escolha uma questão de pesquisa para explorar:", [
        "Qual é o volume de publicações sobre determinado tema ao longo do tempo?",
        "Qual tipo de postagem gera maior número médio de curtidas?",
        "Há correlação entre número de hashtags e número de comentários?",
        "Como varia o número de comentários entre diferentes autores/perfis?",
        "Existe diferença estatística entre engajamento de dois temas?"
    ])

    st.markdown("Faça o upload da base de dados que contenha colunas como 'data', 'tema', 'hashtags', 'comentarios', 'curtidas', 'tipo_postagem', etc.")
    arquivo_simulacao = st.file_uploader("Envie a base (.csv)", type="csv")
    if arquivo_simulacao:
        df_sim = pd.read_csv(arquivo_simulacao)
        st.write("Pré-visualização dos dados:", df_sim.head())

        if questao == "Qual é o volume de publicações sobre determinado tema ao longo do tempo?":
            if 'data' in df_sim.columns:
                df_sim['data'] = pd.to_datetime(df_sim['data'])
                contagem = df_sim.groupby(df_sim['data'].dt.date).size()
                st.line_chart(contagem)

        elif questao == "Qual tipo de postagem gera maior número médio de curtidas?":
            if 'tipo_postagem' in df_sim.columns and 'curtidas' in df_sim.columns:
                medias = df_sim.groupby('tipo_postagem')['curtidas'].mean()
                st.bar_chart(medias)

        elif questao == "Há correlação entre número de hashtags e número de comentários?":
            if 'hashtags' in df_sim.columns and 'comentarios' in df_sim.columns:
                df_sim['n_hashtags'] = df_sim['hashtags'].astype(str).apply(lambda x: len(x.split(',')))
                correlacao = df_sim[['n_hashtags', 'comentarios']].corr()
                st.write("Correlação:", correlacao)

        elif questao == "Como varia o número de comentários entre diferentes autores/perfis?":
            if 'autor' in df_sim.columns and 'comentarios' in df_sim.columns:
                soma_coment = df_sim.groupby('autor')['comentarios'].sum()
                st.bar_chart(soma_coment)

        elif questao == "Existe diferença estatística entre engajamento de dois temas?":
            if 'tema' in df_sim.columns and 'curtidas' in df_sim.columns:
                temas = df_sim['tema'].unique()
                if len(temas) == 2:
                    grupo1 = df_sim[df_sim['tema'] == temas[0]]['curtidas']
                    grupo2 = df_sim[df_sim['tema'] == temas[1]]['curtidas']
                    t_stat, p_val = ttest_ind(grupo1, grupo2, nan_policy='omit')
                    st.write(f"Teste t entre os temas {temas[0]} e {temas[1]}:")
                    st.write(f"Estatística t: {t_stat:.4f}, Valor-p: {p_val:.4f}")
                else:
                    grupos = [df_sim[df_sim['tema'] == t]['curtidas'] for t in temas]
                    f_stat, p_val = f_oneway(*grupos)
                    st.write("ANOVA entre múltiplos temas:")
                    st.write(f"Estatística F: {f_stat:.4f}, Valor-p: {p_val:.4f}")
