# 🚀 Pipeline ETL Automatizado — AWS + Python

Pipeline ETL serverless desenvolvido para extrair dados de uma API pública, transformar com Pandas e carregar no PostgreSQL (AWS RDS).  
Arquivos RAW, processados e logs são armazenados no Amazon S3, com orquestração por EventBridge e execução via Lambda.

Este projeto demonstra arquitetura moderna de dados, boas práticas de engenharia, testes automatizados, infraestrutura como código e escalabilidade utilizando AWS.

---

## 🧩 **Principais Tecnologias**

- **Python 3.11**
- **AWS Lambda**
- **Amazon S3**
- **Amazon RDS (PostgreSQL)**
- **AWS EventBridge**
- **Pandas**
- **SQLAlchemy**
- **Boto3**
- **Pydantic BaseSettings**
- **Pytest**
- **AWS CDK / SAM / Serverless Framework**

---

## 📐 **Arquitetura do Pipeline**

(C:\Users\RUI FRANCISCO\Downloads\mermaid.png)

---

## 📁 **Estrutura do Projeto**

```
etl-pipeline-aws/
│
├── src/
│   ├── extract/
│   │   └── extractor.py
│   ├── transform/
│   │   └── transformer.py
│   ├── load/
│   │   └── loader.py
│   ├── utils/
│   │   ├── logger.py
│   │   └── aws.py
│   ├── main.py
│
├── config/
│   └── settings.py
│
├── tests/
│   ├── test_extractor.py
│   ├── test_transformer.py
│   └── test_loader.py
│
├── infra/
│   ├── cdk/
│   ├── sam/
│   └── serverless/
│
├── Dockerfile
├── requirements.txt
├── .env
├── .gitignore
└── README.md

```

---

## ⚙️ **Configuração do Ambiente**

Crie o arquivo .env na raiz do projeto:
```
ini

API_URL=https://sua-api-publica.com/data
DB_HOST=xxx.amazonaws.com
DB_USER=postgres
DB_PASSWORD=SENHA
DB_NAME=etl_database
DB_PORT=5432

S3_BUCKET=meu-bucket-etl
AWS_REGION=us-east-1
```
O carregamento das variáveis é feito por Pydantic em config/settings.py.

---

## ▶️ **Execução Local**
1. Criar ambiente virtual
```
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
2. Instalar dependências
```
bash
pip install -r requirements.txt
```
3. Rodar o pipeline localmente
```
bash
python src/main.py
```
---
## 🧪 **Testes Automatizados (pytest)**
```
bash
pytest -q
```
Testes cobrem:
- Extração da API (mock requests)
- Transformação com Pandas
- Conexão com banco de dados

---

## 🐳 **Executando com Docker**
Build:
```
bash
docker build -t etl-pipeline .
```
Rodar:
```
bash
docker run --env-file .env etl-pipeline
```
---
## ☁️ **Deploy na AWS**
Escolha sua ferramenta preferida:

- 🚀 Opção 1 — AWS CDK (recomendado)
Instale o CDK:
```
bash
npm install -g aws-cdk
pip install aws-cdk-lib constructs
```
Bootstrap:
```
bash
cd infra/cdk
cdk bootstrap
```
Gerar template:
```
bash
cdk synth
```
Deploy:
```
bash
cdk deploy
```
- 🚀 Opção 2 — AWS SAM
```
bash
cd infra/sam
sam build
sam deploy --guided
```
- 🚀 Opção 3 — Serverless Framework
```
bash
cd infra/serverless
serverless deploy
```
---
## 📌 **Principais Funcionalidades**

- Extração robusta com retry e tratamento de erros
- Transformação com Pandas
- Salvamento de arquivos RAW e processados no S3
- Carregamento em PostgreSQL (RDS)
- Logs estruturados no CloudWatch
- Testes unitários
- Deploy via IaC (CDK / SAM / Serverless)
- Dockerfile para execução local
---
## 🧠 **Práticas Adotadas de Engenharia de Dados**

- Arquitetura Clean (extract/transform/load separados)
- Idempotência no processamento (drop_duplicates)
- Versionamento de dados no S3 com timestamps
- Segregação de ambiente via .env e Pydantic
- Testes com mocks para chamadas externas
- Observabilidade (CloudWatch + logs estruturados)
- Templates de IaC
---
## 📄 **Licença**

Este projeto é distribuído sob a licença MIT.
Sinta-se livre para usar, modificar e evoluir.

---
## 📬 **Contato**
### **Desenvolvido por Rui Francisco de Paula Inácio Diniz**

**_Engenheiro de Software • Desenvolvedor Python • Analista de Dados_**
