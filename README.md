# Pipeline ETL Automatizado — AWS + Python

Pipeline ETL serverless desenvolvido para extrair dados de uma API pública,
transformá-los com Pandas e carregá-los em um banco PostgreSQL (AWS RDS).  
Logs e arquivos de auditoria são armazenados no Amazon S3.

---

## 🧱 Arquitetura

1. **EventBridge** aciona o Lambda (cron ou intervalo definido).
2. **Lambda → Extract:** consumo de API pública com controle de erros.
3. **Transform:** limpeza, normalização e validação usando Pandas.
4. **Load:** inserção em PostgreSQL via SQLAlchemy (upsert/batch).
5. **Auditoria:** arquivos RAW + PROCESSADOS armazenados no S3.
6. **Observabilidade:** logs estruturados (CloudWatch) e versionamento no S3.