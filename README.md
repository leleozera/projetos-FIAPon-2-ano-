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

Este projeto foi desenvolvido como parte do desafio integrador da FIAP, com foco na aplicação de Inteligência Artificial na área da saúde. Ao longo de duas fases, exploramos desde a organização e leitura de diferentes tipos de dados médicos até a construção de um classificador automático de risco clínico.

**Fase 1 — Organização de Dados sobre Doenças Cardiovasculares**
Na primeira parte, o objetivo foi estruturar e organizar diferentes tipos de dados relacionados a doenças cardiovasculares. Foram trabalhados dados em três formatos distintos: dados tabulares (CSV), textos com relatos de sintomas (TXT) e um mapa de conhecimento relacionando sintomas a possíveis doenças. O notebook carrega 10 frases de pacientes descrevendo seus sintomas e um mapa com 24 associações entre sintomas e doenças como Infarto, Arritmia, Angina e Insuficiência Cardíaca. Essa etapa demonstra como dados heterogêneos podem ser coletados, lidos e preparados para uso em projetos de ciência de dados e inteligência artificial na área da saúde.

**Fase 2 — Classificador de Risco Clínico com TF-IDF e Machine Learning**
Na segunda parte, construímos um classificador de texto capaz de analisar frases com descrições de sintomas e classificá-las automaticamente como **alto risco** ou **baixo risco**, simulando o funcionamento de sistemas de triagem clínica automatizada.
Para isso, montamos uma base de dados simulada com 40 frases médicas rotuladas (20 de alto risco e 20 de baixo risco), aplicamos o método **TF-IDF** para transformar as frases em vetores numéricos, e treinamos dois modelos de classificação: **Logistic Regression** e **Decision Tree**. O desempenho dos modelos foi avaliado com métricas como acurácia, precision, recall e F1-score, além de validação cruzada (cross-validation). O projeto inclui também uma etapa de simulação de triagem com frases novas, exibindo o resultado e o nível de confiança de cada classificação.


# 📁 Estrutura do Projeto

- <b>Parte 1</b>: Todo o código para a parte 1 do projeto
- <b>Parte 2</b>: Todo o código para a parte 2 do projeto
- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto

## 🔧 Como executar o código

### Pré-requisitos

- Conta Google (para uso do Google Colab — gratuito, sem instalação local)
- Python 3.10+ (caso queira rodar localmente)
- Bibliotecas: `pandas`, `scikit-learn`, `matplotlib`, `seaborn`

Fase 1: Faça upload do notebook Cap1_Desafio_Integrador.ipynb no Colab junto com os arquivos frasesintomas.txt e mapa_sintomas_doencas.csv, e execute todas as células.

Fase 2: Faça upload do notebook classificador_risco_clinico.ipynb junto com a frases_medicas.csv no Colab, e execute todas as células. 

---

## 🎥 Vídeo de Demonstração

> 📺 https://youtu.be/wv2gI3HQNF8

## 🗃 Histórico de lançamentos

* Parte 1 - 14/04/2026
    * 
* Parte 2 - 14/04/2026
    * 
* Readme - 14/04/2026
    * 
* 0.2.0 - XX/XX/2026
    * 
* 0.1.0 - XX/XX/2026
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


