# Mapa Completo de Campos — Asset `Author` (Exemplo: `A5067237537`)

## 1. Identificação, Nomes e Desambiguação

- `id` (*str*): ex. `https://openalex.org/A5067237537`
- `orcid` (*str*): ex. `https://orcid.org/0000-0003-2999-4961`
- `observed_orcids[]` (*list[str]*): ex. `https://orcid.org/0000-0003-2999-4961`
- `ids.openalex` (*str*): ex. `https://openalex.org/A5067237537`
- `ids.orcid` (*str*): ex. `https://orcid.org/0000-0003-2999-4961`
- `ids.observed_orcids[]` (*list[str]*): ex. `https://orcid.org/0000-0003-2999-4961`
- `display_name` (*str*): ex. `Renato D. Lópes`
- `full_name` (*str*): ex. `Lopes, Renato Delascio`
- `raw_author_names[]` (*list[str]*): ex. `Lopes R`
- `display_name_alternatives[]` (*list[str]*): ex. `Lopes R`
- `block_key` (*str*): ex. `r lopes`

## 2. Afiliações Institucionais (Chaves de Cruzamento)

- `last_known_institutions[]` (*list[dict]*): 8 itens no exemplo
- `last_known_institutions[].id` (*str*): ex. `https://openalex.org/I136199984`
- `last_known_institutions[].ror` (*str*): ex. `https://ror.org/03vek6s52`
- `last_known_institutions[].display_name` (*str*): ex. `Harvard University`
- `last_known_institutions[].country_code` (*str*): ex. `US`
- `last_known_institutions[].type` (*str*): ex. `education`
- `last_known_institutions[].lineage[]` (*list[str]*): ex. `https://openalex.org/I136199984`
- `affiliations[]` (*list[dict]*): 106 itens no exemplo
- `affiliations[].institution.id` (*str*): ex. `https://openalex.org/I110200422`
- `affiliations[].institution.ror` (*str*): ex. `https://ror.org/0176yjw32`
- `affiliations[].institution.display_name` (*str*): ex. `Universidade Federal de Minas Gerais`
- `affiliations[].institution.country_code` (*str*): ex. `BR`
- `affiliations[].institution.type` (*str*): ex. `education`
- `affiliations[].institution.lineage[]` (*list[str]*): ex. `https://openalex.org/I110200422`
- `affiliations[].years[]` (*list[int]*): ex. `2024`

## 3. Área do Conhecimento e Temática

- `topics[]` (*list[dict]*): 5 itens no exemplo
- `topics[].id` (*str*): ex. `https://openalex.org/T10065`
- `topics[].display_name` (*str*): ex. `Atrial Fibrillation Management and Outcomes`
- `topics[].count` (*int*): ex. `486`
- `topics[].subfield.id` (*str*): ex. `https://openalex.org/subfields/2705`
- `topics[].subfield.display_name` (*str*): ex. `Cardiology and Cardiovascular Medicine`
- `topics[].field.id` (*str*): ex. `https://openalex.org/fields/27`
- `topics[].field.display_name` (*str*): ex. `Medicine`
- `topics[].domain.id` (*str*): ex. `https://openalex.org/domains/4`
- `topics[].domain.display_name` (*str*): ex. `Health Sciences`
- `topic_share[]` (*list[dict]*): 5 itens no exemplo
- `topic_share[].id` (*str*): ex. `https://openalex.org/T10065`
- `topic_share[].display_name` (*str*): ex. `Atrial Fibrillation Management and Outcomes`
- `topic_share[].value` (*float*): ex. `0.0019535`
- `topic_share[].subfield.id` (*str*): ex. `https://openalex.org/subfields/2705`
- `topic_share[].subfield.display_name` (*str*): ex. `Cardiology and Cardiovascular Medicine`
- `topic_share[].field.id` (*str*): ex. `https://openalex.org/fields/27`
- `topic_share[].field.display_name` (*str*): ex. `Medicine`
- `topic_share[].domain.id` (*str*): ex. `https://openalex.org/domains/4`
- `topic_share[].domain.display_name` (*str*): ex. `Health Sciences`
- `x_concepts[]` (*list[dict]*): 5 itens no exemplo
- `x_concepts[].id` (*str*): ex. `71924100`
- `x_concepts[].wikidata` (*str*): ex. `https://www.wikidata.org/wiki/Q11190`
- `x_concepts[].display_name` (*str*): ex. `Medicine`
- `x_concepts[].score` (*float*): ex. `0.9941516518592834`

## 4. Métricas de Produção, Impacto e Financiamento

- `works_count` (*int*): ex. `1327`
- `cited_by_count` (*int*): ex. `75911`
- `summary_stats.2yr_mean_citedness` (*float*): ex. `10.964285714285714`
- `summary_stats.h_index` (*int*): ex. `121`
- `summary_stats.i10_index` (*int*): ex. `601`
- `counts_by_year[]` (*list[dict]*): 23 itens no exemplo
- `counts_by_year[].year` (*int*): ex. `1999`
- `counts_by_year[].works_count` (*int*): ex. `1`
- `counts_by_year[].oa_works_count` (*int*): ex. `1`
- `counts_by_year[].cited_by_count` (*int*): ex. `0`
- `works_api_url` (*str*): ex. `https://api.openalex.org/works?filter=author.id:A506723`
- `awards_count` (*int*): ex. `0`
- `awards_api_url` (*str*): ex. `https://api.openalex.org/awards?filter=investigators.au`

## 5. Metadados de Controle

- `created_date` (*str*): ex. `2016-06-24T00:00:00`
- `updated_date` (*str*): ex. `2026-11-21T13:19:37`
