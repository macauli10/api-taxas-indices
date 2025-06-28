# 📊 Projeto de Engenharia de Dados: Taxas de Juros com BrasilAPI

Este projeto tem como objetivo realizar a **extração contínua de dados financeiros** da [BrasilAPI](https://brasilapi.com.br/), armazená-los localmente em um banco de dados **SQLite**, e exibir as informações de forma visual e interativa por meio de um **dashboard com Streamlit**. Toda a aplicação está **containerizada com Docker** para facilitar a execução e o deploy.

---

## 🚀 Funcionalidades

✅ Coleta de dados em tempo real (a cada 10 segundos) da BrasilAPI  
✅ Armazenamento dos dados em banco de dados SQLite  
✅ Dashboard moderno com Streamlit (modo dark, gráficos, métricas)  
✅ Containerização com Docker e orquestração com Docker Compose  
✅ Código limpo, comentado e organizado para reuso ou expansão  

---

## 🧱 Tecnologias Utilizadas

- **Python 3.12**
- **SQLite 3**
- **Streamlit** (dashboard web)
- **Pandas + Requests**
- **Altair** (gráficos interativos)
- **Docker + Docker Compose**

---

## 🧩 Estrutura do Projeto

api-financeiro/
├── app.py # Coletor contínuo de dados da API
├── app_streamlit.py # Dashboard interativo com Streamlit
├── Dockerfile
├── docker-compose.yaml # Orquestrador dos dois serviços
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

yaml
Copy
Edit

---

## 🔍 Visão Geral das Etapas

### 📥 Extração de Dados da API
O script `app.py` faz requisições para a [BrasilAPI](https://brasilapi.com.br/api/taxas/v1) a cada 10 segundos e salva as taxas de juros como **SELIC, CDI e IPCA** no banco SQLite.

### 🛢️ Armazenamento com SQLite
Todos os dados coletados são armazenados em uma tabela chamada `taxas`, com campos como `nome`, `valor` e `data`. É possível fazer consultas manuais via SQL para análises.

### 📊 Visualização com Streamlit
O script `app_streamlit.py` lê o banco SQLite e apresenta os dados em tempo real com:

- Métricas de SELIC, CDI, IPCA
- Gráfico de barras com Altair
- Tabela interativa dos valores
- Modo escuro e layout responsivo


---

## ⚙️ Como Executar

### 1. Clone o projeto

```bash
git clone https://github.com/macauli10/api-taxas-indices.git
cd api-financeiro