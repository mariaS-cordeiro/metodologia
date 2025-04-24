"Abordagem Quantitativa",
"Estudo de Caso",
"Base de Dados Textuais",
    "Base com Vídeos"
    "Base com Vídeos",
    "Simulações Quantitativas"
])

# ----------- ABA QUALITATIVA ----------- #
@@ -75,3 +76,46 @@
st.text_area("Anotação sobre este trecho do vídeo")
if st.button("Salvar anotação do vídeo"):
st.success("Anotação registrada com sucesso!")

# ----------- ABA SIMULAÇÕES QUANTITATIVAS ----------- #
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
            st.write("⚠️ Essa análise requer tratamento estatístico adicional (teste t, ANOVA, etc.). Podemos implementá-la em uma versão futura.")
