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
- <a href="https://www.linkedin.com/company/inova-fusca">André Godoi</a>


## 📜 Descrição

🧩 Problema

Os relatórios genéticos fornecidos pelo Genera (Dasa) são entregues em formato PDF com grande volume de informações técnicas, linguagem científica e baixa interatividade.

Isso dificulta a compreensão por parte dos pacientes, que muitas vezes não possuem conhecimento na área da saúde para interpretar corretamente os dados apresentados, como níveis de risco para doenças, predisposições genéticas e recomendações implícitas.

Como consequência, o usuário pode:
- Não entender a gravidade ou relevância das informações;
- Interpretar os dados de forma incorreta;
- Não saber quais ações tomar a partir do resultado.

Além disso, o formato atual não permite exploração interativa dos dados, nem a possibilidade de realizar perguntas específicas sobre o próprio exame.

Dessa forma, há uma lacuna entre a disponibilidade de dados e a capacidade do usuário de transformá-los em conhecimento útil para tomada de decisão.

---

💡 Solução

Propomos o desenvolvimento de uma plataforma inteligente baseada em Inteligência Artificial capaz de transformar relatórios genéticos em uma experiência interativa, acessível e personalizada.

A solução realiza o upload do PDF do exame e executa um pipeline de processamento que extrai, organiza e estrutura os dados em um formato compreensível.

A partir disso, o sistema oferece:

- Explicações simplificadas dos resultados;
- Chat interativo com IA;
- Recomendações personalizadas com foco em prevenção;
- Dashboard visual para melhor entendimento dos dados.

Com isso, a solução transforma dados complexos em conhecimento acionável.

---

## 👥 Usuários

### 👤 Paciente
- Entender resultados em linguagem simples;
- Saber nível de risco;
- Receber recomendações práticas;
- Tirar dúvidas com IA.

### 👨‍⚕️ Médico
- Acesso rápido a dados relevantes;
- Apoio na tomada de decisão.

### 🏢 Dasa
- Melhorar experiência do usuário;
- Reduzir dúvidas;
- Agregar valor ao produto.

---

# 📊 Estrutura dos dados

```json
{
  "paciente": {
    "id": "12345",
    "nome": "Exemplo"
  },
  "relatorio": [
    {
      "condicao": "Diabetes Tipo 2",
      "categoria": "Metabolismo",
      "risco": "Alto",
      "descricao": "Predisposição genética identificada.",
      "recomendacoes": [
        "Praticar exercícios",
        "Manter dieta equilibrada"
      ]
    }
  ]
}

```
---

## ⚙️ Pipeline de Dados

1. Upload do PDF  
2. Extração de texto  
3. Limpeza e processamento  
4. Estruturação em JSON  
5. Uso pela IA  

---

## 🤖 Inteligência Artificial

A solução utiliza LLM com abordagem RAG.

Funcionamento:
1. Dados estruturados são processados;
2. IA busca informações relevantes;
3. Responde com base no exame;
4. Gera respostas claras e personalizadas.

Exemplos de perguntas:
- "Tenho risco alto?"
- "O que significa isso?"
- "O que posso fazer?"

---

## 🏗️ Arquitetura (Diagrama)

<img width="1060" height="695" alt="image" src="https://github.com/user-attachments/assets/dc272e24-4d2d-4e46-87d6-25739494b46e" />

---

## 🧠 Tecnologias

- Python (processamento)
- PyPDF / pdfplumber
- FastAPI / Flask
- LLM (API)
- JSON
- React / Streamlit

---


## 🎥 Vídeo 

> 📺 

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

