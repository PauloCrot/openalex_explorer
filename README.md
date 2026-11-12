# OpenAlex Explorer (Protótipo)

Protótipo desenvolvido no âmbito de Iniciação Científica para extração, normalização e análise exploratória de metadados científicos da América Latina utilizando a API REST.

> **Status:** Protótipo inicial (v0.1) focado na entidade `Works` (publicações e redes de coautoria).

## Fase Atual

- **Pipeline ETL Modular:** Extração via API (`extract`), normalização de JSONs aninhados e arrays de autores/países (`transform`) e exportação tabular (`load`).
- **Interface CLI Interativa:** Menu via terminal com tratamento de erros HTTP e opção de cancelamento a qualquer momento.
- **Modos de Consulta:**
  - Coautoria direta (`AND`) entre pares de países.
  - Produção científica por lista de países.
  - Filtragem por tópico (via ID do OpenAlex ou busca interativa por palavra-chave).
  - Tabela de referência rápida com códigos ISO 3166-1 alpha-2 da América Latina.
- Amostragem e Persistência Segura: Suporte a extração por amostragem aleatória (`sample`) ou ordenação por citações, salvando os resultados em `output/` com versionamento automático (`_1`, `_2`, ...) para evitar sobrescrita de dados.

## Estrutura do Projeto

```text
openalex_explorer/
├── main.py              # Ponto de entrada da aplicação
├── requirements.txt     # Dependências do projeto
└── src/
    ├── config.py        # Configurações globais e códigos ISO LatAm
    ├── api/             # Cliente HTTP (Polite Pool do OpenAlex)
    ├── cli/             # Menu interativo, utilitários e handlers
    └── etl/             # Extração, transformação, carga e orquestração

## Modo de Execução

```bash
# 1. Crie e ative o ambiente virtual
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate # Linux/macOS

# 2. Instale as dependências e rode o programa
pip install -r requirements.txt
python main.py
```