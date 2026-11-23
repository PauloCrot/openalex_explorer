# OpenAlex Explorer (Protótipo)

Protótipo desenvolvido no âmbito de Iniciação Científica para extração, normalização e análise exploratória de metadados científicos da América Latina utilizando a API REST do OpenAlex.

> **Status:** Etapa 2 - mapeamento de metadados e validação de filtros para `Works`, `Institutions` e `Authors` (integração de `Institutions` e `Authors` no menu CLI em andamento).

## Funcionalidades e Entregas

- **Mapeamento de Metadados (`docs/schemas/`):** Inventário completo e categorizado dos campos e chaves de cruzamento para `Work`, `Institution` e `Author`, acompanhado de validação de volumetria geográfica (Brasil, América do Sul).
- **Pipeline ETL Modular (`src/`):** Extração via API (`extract`), normalização de JSONs aninhados (`transform` + `parsers`) e exportação tabular (`load`) com versionamento automático em `output/` (`_1`, `_2`, ...).
- **Interface CLI Interativa:** Menu via terminal com tratamento de erros HTTP, amostragem (`sample` ou ordenação por citações) e opção de cancelamento (`c` / `cancelar`) para consultas de `Works` (coautoria `AND`, lista de países `OR`, tópicos e códigos ISO da LatAm).

## Estrutura do Projeto

```text
openalex_explorer/
├── main.py              # Ponto de entrada da aplicação CLI
├── requirements.txt     # Dependências do projeto
├── docs/
│   └── schemas/         # Inventários de campos (Work, Institution, Author)
├── scripts/             # Inspeção de assets brutos e validação de filtros
└── src/
    ├── config.py        # Configurações globais e códigos ISO LatAm
    ├── api/             # Cliente HTTP (Polite Pool do OpenAlex)
    ├── cli/             # Menu interativo, utilitários e handlers
    ├── etl/             # Extração, transformação, carga e orquestração
    ├── filters/         # Montagem de queries por país e tópico
    └── parsers/         # Achata JSONs brutos (Work, Institution, Author)

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