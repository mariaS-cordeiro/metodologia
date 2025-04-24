Skip to content
Navigation Menu
mariaS-cordeiro
metodologia

Type / to search
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Commit 7697603
mariaS-cordeiro
mariaS-cordeiro
authored
last week
Verified
Update mestrado.py
main
1 parent 
152ab40
 commit 
7697603
File tree
Filter files…
mestrado.py
1 file changed
+49
-36
lines changed
Search within code
 
Customizable line height
The default line height has been increased for improved accessibility. You can choose to enable a more compact line height from the view settings menu.

‎mestrado.py
+49
-36
Original file line number	Diff line number	Diff line change
@@ -1,6 +1,7 @@
import streamlit as st
import pandas as pd
from datetime import datetime
from scipy.stats import ttest_ind, f_oneway

st.set_page_config(page_title="Ambiente de Metodologia de Pesquisa", layout="wide")

@@ -43,7 +44,42 @@
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

@@ -84,39 +120,16 @@
                st.bar_chart(soma_coment)

        elif questao == "Existe diferença estatística entre engajamento de dois temas?":
            st.write("⚠️ Essa análise requer tratamento estatístico adicional (teste t, ANOVA, etc.). Podemos implementá-la em uma versão futura.")
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
0 commit comments
Comments
0
 (0)
Comment
You're receiving notifications because you're subscribed to this thread.

Update mestrado.py · mariaS-cordeiro/metodologia@7697603
