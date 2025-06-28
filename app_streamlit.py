import streamlit as st
import sqlite3
import pandas as pd
import altair as alt
st.set_page_config(page_title="Dashboard de Taxas - BrasilAPI", layout="wide")

st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Segoe UI', sans-serif;
            background-color: #0E1117;
            color: #FFFFFF;
        }
        .stDataFrame { background-color: #1C1C1C; }
    </style>
""", unsafe_allow_html=True)


conn = sqlite3.connect('dados_financeiros.db')
df = pd.read_sql_query('SELECT * FROM taxas ORDER BY data DESC', conn)
conn.close()

df_latest = df.sort_values('data').drop_duplicates('nome', keep='last')
df_latest = df_latest.sort_values('valor', ascending=False)


st.title('📊 Dashboard das Taxas de Juros - BrasilAPI')


col1, col2, col3 = st.columns(3)
with col1:
    selic = df_latest[df_latest['nome'] == 'Selic']['valor'].values[0]
    st.metric("📈 SELIC", f"{selic:.2f}%")
with col2:
    cdi = df_latest[df_latest['nome'] == 'CDI']['valor'].values[0]
    st.metric("💵 CDI", f"{cdi:.2f}%")
with col3:
    ipca = df_latest[df_latest['nome'] == 'IPCA']['valor'].values[0]
    st.metric("📉 IPCA", f"{ipca:.2f}%")

st.markdown("---")


st.subheader("📊 Comparação das Taxas (gráfico de barras)")

chart = alt.Chart(df_latest).mark_bar().encode(
    x=alt.X('valor:Q', title='Valor (%)'),
    y=alt.Y('nome:N', sort='-x', title='Tipo de Taxa'),
    color=alt.Color('nome:N', legend=None),
    tooltip=['nome', 'valor']
).properties(
    width=700,
    height=300
).configure_axis(
    labelColor='white',
    titleColor='white'
).configure_view(
    stroke=None
).configure_title(
    color='white'
)

st.altair_chart(chart, use_container_width=True)

st.subheader("📋 Tabela de valores mais recentes")
st.dataframe(df_latest.style.format({"valor": "{:.2f}"}), height=300, use_container_width=True)


with st.expander("📚 Ver histórico completo"):
    st.dataframe(df.sort_values("data", ascending=False), height=300)
