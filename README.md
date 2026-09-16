# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Leonardo Nunes Urbano</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Erick Souza Pereira</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Caique Nonato</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoir</a>


## Descrição

Nesta Fase 5 o projeto CardioIA avança das fases anteriores (monitoramento e visão computacional) para um **Assistente Cardiológico Inteligente e Conversacional**, capaz de:

- Interagir com o usuário por linguagem natural, simulando um atendimento inicial em saúde;
- Interpretar a mensagem do usuário via **IBM Watson Assistant** (intents, entities e dialog nodes);
- Repassar a conversa por um **backend em Flask**, que faz a ponte entre a interface e a API do Watson;
- Apresentar tudo em uma **interface web simples de chat**.

O assistente **não substitui atendimento médico** — seu papel é orientar, fazer uma triagem inicial de sintomas e indicar quando procurar ajuda profissional (inclusive sinalizando urgência).

## Arquitetura

```
Usuário → frontend/index.html → backend Flask (/chat) → IBM Watson Assistant (API v2) → resposta
```

## Estrutura de pastas

```
├── 📁 backend/
│   ├── app.py                          # Rotas Flask (/health, /session, /chat)
│   ├── watson_client.py                # Wrapper de integração com o Watson Assistant
│   ├── config.py                       # Carregamento de credenciais via .env
│   ├── requirements.txt
│   └── .env.example
│
├── 📁 frontend/
│   └── index.html                      # Interface de chat (HTML + JS puro)
│
├── 📄 cardioia-assistente-skill.json   # Exportação do skill do Watson Assistant (intents/entities/dialog nodes)
 ── 📄 relatorio-fluxo-conversacional.docx  # Relatório do fluxo conversacional

```

## Passo a passo para testar AGORA (modo simulação, sem Watson)

Pra ver o chat funcionando de ponta a ponta antes de configurar o Watson de verdade:

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Sem um `.env` preenchido, o backend detecta isso automaticamente e entra em
**SIMULATION_MODE** (aviso aparece no terminal), respondendo com uma lógica
local equivalente ao skill, sem depender do IBM Cloud. Com o backend rodando
em `http://localhost:5000`, é só abrir `frontend/index.html` no navegador e
conversar.

> Isso é só para desenvolvimento/teste. O entregável final precisa estar
> conversando com o Watson Assistant de verdade (veja a seção abaixo).

## Como configurar o Watson Assistant

1. Crie uma instância do **Watson Assistant** no [IBM Cloud](https://cloud.ibm.com).
2. Crie um novo Assistant e importe o arquivo `cardioia-assistente-skill.json` como skill (Assistant → Skills → Import skill).
3. Publique o skill no ambiente (draft ou live) e anote:
   - a **API Key** (Manage → API details)
   - a **Service URL**
   - o **Assistant ID** (ou Environment ID)
4. Preencha essas informações no arquivo `.env` do backend (veja `.env.example`).

## Como executar o backend

```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # depois edite com suas credenciais reais
python app.py
```

O backend sobe em `http://localhost:5000`.

## Como executar a interface

Basta abrir `frontend/index.html` no navegador (ou servir com qualquer servidor estático). Por padrão a interface aponta para `http://localhost:5000`; ajuste a constante `API_BASE_URL` no `index.html` se o backend estiver em outro endereço.


## Vídeo demonstrativo

https://youtu.be/Tio_-t0T52k

    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


