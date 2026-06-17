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

O objetivo geral dessa atividade é construir um protótipo de Assistente Cardiológico Virtual que atenda os seguintes requisitos:

-Realizar o pré-processamento de imagens médicas simuladas (exemplo: ECGs, raios-X ou datasets públicos de saúde). Nós utilizamos o dataset MedMNIST, que é uma coleção com vários subconjuntos (olho, tórax, patologia, dermatologia, etc.), com imagens de muitas classes diferentes. É o mais diverso e completo, com até 18 datasets médicos padronizados em um só pacote.

-Treinar e avaliar modelos de CNN para classificar e identificar padrões em imagens médicas.

-Apresentar os resultados de forma acessível em uma aplicação simples, como por exemplo um notebook interativo, priorizando clareza e facilidade de interpretação dos resultados obtidos pelo modelo.

-Utilize do trabalho em equipe e da colaboração interdisciplinar — Estimulando habilidades de comunicação, cooperação e divisão equilibrada de tarefas. O trabalho em equipe é considerado uma soft skill essencial para o ambiente profissional e acadêmico.



## 📁 Estrutura de pastas

```

📁 processamento-imagens-medicas/
│
├── 📁 .config/                         # Configurações do ambiente Colab
│
├── 📁 data/
│   └── 📦 bloodmnist.npz               # Dataset BloodMNIST baixado automaticamente
│
├── 📁 sample_data/                      # Dados de exemplo padrão do Colab
│   ├── 📄 README.md
│   ├── anscombe.json
│   ├── california_housing_test.csv
│   ├── california_housing_train.csv
│   ├── mnist_test.csv
│   └── mnist_train_small.csv
│
├── 🖼️ amostras_brutas.png              # Visualização das amostras originais
├── 🖼️ antes_depois.png                 # Comparação pré/pós processamento
├── 🖼️ distribuicao_classes.png         # Gráfico de distribuição por classe
└── 📋 pipeline_info.json               # Parâmetros de normalização salvos

```

> **Nota:** A pasta `.config` e `sample_data` são geradas automaticamente pelo Google Colab e podem ser ignoradas no `.gitignore`.


## 🔧 Como executar o código (Parte 1)

1. Faça o upload do arquivo `parte1_medmnist.ipynb` no [Google Colab](https://colab.research.google.com/)
2. Execute a primeira célula para instalar as dependências automaticamente
3. Rode as células em ordem — o dataset BloodMNIST será baixado automaticamente
4. Ao final, os arquivos `pipeline_info.json` e os gráficos `.png` serão salvos na sessão do Colab

> **Requisitos:** Conta Google. Nenhuma instalação local necessária.

## 🔧 Como executar o código (Parte 2)

1. Faça o upload do arquivo parte2_cnn_classificacao.ipynb no Google Colab
2. Execute a primeira célula para instalar as dependências automaticamente
3. Rode as células em ordem — o pipeline da Parte 1 é reconstruído automaticamente (download do BloodMNIST, normalização e augmentação)
4. As células seguintes treinam a CNN do zero e o modelo de Transfer Learning (ResNet18), nessa ordem
5. Ao final, são exibidos as métricas de avaliação (acurácia, precisão, recall, F1-score), as matrizes de confusão de cada modelo, o gráfico comparativo entre as duas abordagens e o protótipo de visualização das predições


> **Requisitos:** Conta Google. Recomenda-se ativar GPU em Ambiente de execução → Alterar tipo de ambiente de execução → GPU, para acelerar o treinamento.


## 🗃 Histórico de lançamentos

* 0.5.0 - XX/XX/2026
    * 
* 0.4.0 - XX/XX/2026
    * 
* 0.3.0 - XX/XX/2026
    * 
* 0.2.0 - XX/XX/2026
    * 
* 0.1.0 - XX/XX/2026
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


