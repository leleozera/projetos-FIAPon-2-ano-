# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# 🌌 Galax IA — Monitoramento Inteligente de Objetos Próximos à Terra

---

## 👩🏻‍💻 Integrantes

| Nome | RM |
|------|-----|
| Erick Souza | RM 564996 |
| Leonardo Nunes | RM 565518 |

---

## 📚 Sobre o Projeto

O **Galax IA** é uma aplicação web de monitoramento de objetos próximos à Terra (NEOs — Near-Earth Objects), desenvolvida como solução para o desafio **Global Solutions da FIAP**.

A solução integra:
- 📡 Dados em tempo real da **NASA NeoWs API**
- 🤖 **Machine Learning** com K-Means para clusterização dos objetos
- 💬 **IA Generativa** com LLaMA 3.3 via Groq, usando o padrão **RAG**
- 📊 Dashboard interativo com gráficos e tabelas

---

## 🎯 Problema e Solução

**Problema:** Asteroides e objetos espaciais se aproximam da Terra diariamente, mas as informações disponíveis são técnicas e de difícil acesso para o público geral.

**Solução:** Uma plataforma que coleta, processa e apresenta esses dados de forma visual e interativa, com um assistente de IA capaz de responder perguntas em linguagem natural com base nos dados reais do momento.

---

## 🗂️ Estrutura do Repositório

```bash
📂 global-solutions-galaxia
│
├── 📂 backend
│   ├── main.py              # API REST com FastAPI
│   ├── data_collector.py    # Coleta de dados NASA NeoWs
│   ├── analyzer.py          # Machine Learning (K-Means)
│   ├── rag.py               # IA Generativa com RAG (Groq / LLaMA)
│   └── requirements.txt     # Dependências Python
│  
│
├── 📂 astrosight-web
│   ├── 📂 src
│   │   ├── App.jsx           # Componente principal
│   │   ├── index.css         # Estilos globais
│   │   └── main.jsx          # Entry point React
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Versão | Uso |
|---|---|---|
| Python | 3.12 | Backend principal |
| FastAPI | latest | API REST |
| scikit-learn | latest | K-Means clustering |
| pandas | latest | Manipulação de dados |
| Groq API (LLaMA 3.3 70B) | — | IA Generativa gratuita |
| React | 19 | Frontend SPA |
| Vite | latest | Build tool |
| Recharts | latest | Gráficos interativos |
| NASA NeoWs API | — | Fonte dos dados de asteroides |

---

## ▶️ Como Executar

### Pré-requisitos
- Python 3.12+
- Node.js 18+
- Chaves de API: [NASA](https://api.nasa.gov) e [Groq](https://console.groq.com)

### Backend

```bash
# Acesse a pasta do backend
cd backend

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# Instale as dependências
pip install -r requirements.txt

# Configure as variáveis de ambiente

# Inicie o servidor
uvicorn main:app --reload
```

O backend estará disponível em `http://localhost:8000`

### Frontend

```bash
# Acesse a pasta do frontend
cd astrosight-web

# Instale as dependências
npm install

# Inicie o servidor de desenvolvimento
npm run dev
```

O frontend estará disponível em `http://localhost:5173`

---

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` dentro da pasta `backend`:

```env
GROQ_API_KEY=sua_chave_aqui
```

---

## 🌐 Endpoints da API

| Endpoint | Método | Descrição |
|---|---|---|
| `/` | GET | Status da API |
| `/dados` | GET | NEOs dos últimos 7 dias |
| `/analise` | GET | Estatísticas + clusters K-Means |
| `/chat` | POST | Pergunta → resposta IA com RAG |

---

## 🎬 Vídeo de Demonstração

> 📹 [Inserir link do vídeo após gravação]

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/SabrinaOtoni/TEMPLATE-FIAP-GRAD-ON-IA">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">FIAP</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
