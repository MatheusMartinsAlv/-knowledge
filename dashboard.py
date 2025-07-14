# ficheiro: dashboard.py

import streamlit as st
import pandas as pd
import numpy as np

# --- Título e Configuração da Página ---
st.set_page_config(layout="wide", page_title="+KNOWLEDGE - Dashboard de Vendas")

st.title("📊 Dashboard de Análise de Vendas")
st.markdown("Bem-vindo ao seu painel de controle. Aqui pode analisar a performance dos seus produtos.")

# --- Simulação de Dados ---
dados = {
    'Produto': [
        'Xadrez para Iniciantes', 'Desenvolvimento Web Moderno', 'Inglês Básico', 'Xadrez para Iniciantes',
        'Desenvolvimento Web Moderno', 'Xadrez para Iniciantes', 'Inglês Básico', 'Desenvolvimento Web Moderno',
        'Xadrez para Iniciantes'
    ],
    'Categoria': [
        'Estratégia', 'Tecnologia', 'Idiomas', 'Estratégia',
        'Tecnologia', 'Estratégia', 'Idiomas', 'Tecnologia',
        'Estratégia'
    ],
    'Preço': [
        49.90, 199.90, 0.00, 49.90,
        199.90, 49.90, 0.00, 199.90,
        49.90
    ],
    'Data Venda': pd.to_datetime([
        '2025-07-01', '2025-07-02', '2025-07-02', '2025-07-03',
        '2025-07-04', '2025-07-05', '2025-07-05', '2025-07-06',
        '2025-07-07'
    ])
}
df = pd.DataFrame(dados)

# --- Métricas Principais ---
st.header("Visão Geral")
total_receita = df['Preço'].sum()
total_vendas = len(df)
preco_medio = df['Preço'][df['Preço'] > 0].mean()

col1, col2, col3 = st.columns(3)
col1.metric("Receita Total", f"R$ {total_receita:,.2f}", "📈")
col2.metric("Total de Vendas", f"{total_vendas}", "🛒")
col3.metric("Preço Médio (pago)", f"R$ {preco_medio:,.2f}", "💰")

st.markdown("---")

# --- Análises com Gráficos ---
st.header("Análise Detalhada")

# Filtro por Categoria
categorias = ['Todas'] + list(df['Categoria'].unique())
categoria_selecionada = st.selectbox("Filtrar por Categoria:", categorias)

if categoria_selecionada != 'Todas':
    df_filtrado = df[df['Categoria'] == categoria_selecionada]
else:
    df_filtrado = df

# Gráfico de Vendas por Produto
st.subheader("Vendas por Produto")
vendas_por_produto = df_filtrado['Produto'].value_counts()
st.bar_chart(vendas_por_produto)

# Tabela de Dados
st.subheader("Dados Brutos das Vendas")
st.dataframe(df_filtrado)
