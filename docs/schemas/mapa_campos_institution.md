# Mapa Completo de Campos — Asset `Institution` (Exemplo: `I88273585`)

## 1. Identificação e Nomes

- `id` (*str*): ex. `https://openalex.org/I88273585`
- `ror` (*str*): ex. `https://ror.org/02k5swt12`
- `ids.openalex` (*str*): ex. `https://openalex.org/I88273585`
- `ids.ror` (*str*): ex. `https://ror.org/02k5swt12`
- `ids.grid` (*str*): ex. `grid.411249.b`
- `ids.wikipedia` (*str*): ex. `http://en.wikipedia.org/wiki/Federal_University_of_S%C3`
- `ids.wikidata` (*str*): ex. `https://www.wikidata.org/wiki/Q4384447`
- `display_name` (*str*): ex. `Universidade Federal de São Paulo`
- `display_name_acronyms[]` (*list[str]*): ex. `UNIFESP`
- `display_name_alternatives[]` (*list[str]*): ex. `Federal University of São Paulo`
- `homepage_url` (*str*): ex. `https://portal.unifesp.br/`
- `image_url` (*str*): ex. `https://commons.wikimedia.org/w/index.php?title=Special`
- `image_thumbnail_url` (*str*): ex. `https://commons.wikimedia.org/w/index.php?title=Special`

## 2. Localização Geográfica e Classificação

- `country_code` (*str*): ex. `BR`
- `type` (*str*): ex. `education`
- `type_id` (*str*): ex. `https://openalex.org/institution-types/education`
- `geo.city` (*str*): ex. `São Paulo`
- `geo.geonames_city_id` (*str*): ex. `3448439`
- `geo.region` (*str*): ex. `São Paulo`
- `geo.country_code` (*str*): ex. `BR`
- `geo.country` (*str*): ex. `Brazil`
- `geo.latitude` (*float*): ex. `-23.5475`
- `geo.longitude` (*float*): ex. `-46.63611`

## 3. Hierarquia e Relações Institucionais (Chaves de Cruzamento)

- `associated_institutions[]` (*list[dict]*): 2 itens no exemplo
- `associated_institutions[].id` (*str*): ex. `https://openalex.org/I4210162743`
- `associated_institutions[].ror` (*str*): ex. `https://ror.org/050z9fj14`
- `associated_institutions[].display_name` (*str*): ex. `Hospital São Paulo`
- `associated_institutions[].country_code` (*str*): ex. `BR`
- `associated_institutions[].type` (*str*): ex. `healthcare`
- `associated_institutions[].relationship` (*str*): ex. `related`
- `lineage[]` (*list[str]*): ex. `https://openalex.org/I88273585`
- `repositories[]` (*list[dict]*): 1 itens no exemplo
- `repositories[].id` (*str*): ex. `https://openalex.org/S4377196380`
- `repositories[].display_name` (*str*): ex. `UNIFESP Institutional Repository (Universidade Federal `
- `repositories[].host_organization` (*str*): ex. `https://openalex.org/I88273585`
- `repositories[].host_organization_name` (*str*): ex. `Universidade Federal de São Paulo`
- `repositories[].host_organization_lineage[]` (*list[str]*): ex. `https://openalex.org/I88273585`
- `roles[]` (*list[dict]*): 3 itens no exemplo
- `roles[].role` (*str*): ex. `funder`
- `roles[].id` (*str*): ex. `https://openalex.org/F4320318003`
- `roles[].works_count` (*int*): ex. `290`

## 4. Área do Conhecimento e Temática

- `topics[]` (*list[dict]*): 25 itens no exemplo
- `topics[].id` (*str*): ex. `https://openalex.org/T10316`
- `topics[].display_name` (*str*): ex. `Sleep and related disorders`
- `topics[].count` (*int*): ex. `1911`
- `topics[].score` (*float*): ex. `1.0`
- `topics[].subfield.id` (*str*): ex. `https://openalex.org/subfields/3205`
- `topics[].subfield.display_name` (*str*): ex. `Experimental and Cognitive Psychology`
- `topics[].field.id` (*str*): ex. `https://openalex.org/fields/32`
- `topics[].field.display_name` (*str*): ex. `Psychology`
- `topics[].domain.id` (*str*): ex. `https://openalex.org/domains/2`
- `topics[].domain.display_name` (*str*): ex. `Social Sciences`
- `topic_share[]` (*list[dict]*): 25 itens no exemplo
- `topic_share[].id` (*str*): ex. `https://openalex.org/T10312`
- `topic_share[].display_name` (*str*): ex. `Health, Nursing, Elderly Care`
- `topic_share[].value` (*float*): ex. `0.0188583`
- `topic_share[].subfield.id` (*str*): ex. `https://openalex.org/subfields/3600`
- `topic_share[].subfield.display_name` (*str*): ex. `General Health Professions`
- `topic_share[].field.id` (*str*): ex. `https://openalex.org/fields/36`
- `topic_share[].field.display_name` (*str*): ex. `Health Professions`
- `topic_share[].domain.id` (*str*): ex. `https://openalex.org/domains/4`
- `topic_share[].domain.display_name` (*str*): ex. `Health Sciences`

## 5. Métricas de Produção, Impacto e Financiamento

- `works_count` (*int*): ex. `107662`
- `works_count_with_children` (*int*): ex. `107691`
- `works_count_with_children_and_predecessors` (*int*): ex. `107691`
- `cited_by_count` (*int*): ex. `2231809`
- `summary_stats.2yr_mean_citedness` (*float*): ex. `2.5816319271537314`
- `summary_stats.h_index` (*int*): ex. `385`
- `summary_stats.i10_index` (*int*): ex. `38191`
- `counts_by_year[]` (*list[dict]*): 17 itens no exemplo
- `counts_by_year[].year` (*int*): ex. `2026`
- `counts_by_year[].works_count` (*int*): ex. `6109`
- `counts_by_year[].oa_works_count` (*int*): ex. `5089`
- `counts_by_year[].cited_by_count` (*int*): ex. `202241`
- `works_api_url` (*str*): ex. `https://api.openalex.org/works?filter=institutions.id:I`
- `awards_count` (*int*): ex. `5207`
- `awards_api_url` (*str*): ex. `https://api.openalex.org/awards?filter=institution_awar`

## 6. Metadados de Controle

- `is_super_system` (*bool*): ex. `False`
- `status` (*str*): ex. `active`
- `created_date` (*str*): ex. `2016-06-24T00:00:00`
- `updated_date` (*str*): ex. `2026-11-20T18:22:16`
