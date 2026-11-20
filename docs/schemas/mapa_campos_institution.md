# Mapa Completo de Campos — Asset `Institution` (Exemplo: `I4210118976`)

## 1. Identificação e Nomes

- `id` (*str*): ex. `https://openalex.org/I4210118976`
- `ror` (*str*): ex. `https://ror.org/02zyjt610`
- `ids.openalex` (*str*): ex. `https://openalex.org/I4210118976`
- `ids.ror` (*str*): ex. `https://ror.org/02zyjt610`
- `ids.grid` (*str*): ex. `grid.426567.4`
- `ids.wikipedia` (*NoneType*): ex. `None`
- `ids.wikidata` (*str*): ex. `https://www.wikidata.org/wiki/Q30285577`
- `display_name` (*str*): ex. `Veterinary Research Institute`
- `display_name_acronyms[]` (*list[str]*): ex. `VRI`
- `display_name_alternatives[]` (*list[str]*): ex. `Veterinary Research Institute`
- `homepage_url` (*str*): ex. `https://www.vri.cz/`
- `image_url` (*NoneType*): ex. `None`
- `image_thumbnail_url` (*NoneType*): ex. `None`

## 2. Localização Geográfica e Classificação

- `country_code` (*str*): ex. `CZ`
- `type` (*str*): ex. `facility`
- `type_id` (*str*): ex. `https://openalex.org/institution-types/facility`
- `geo.city` (*str*): ex. `Brno`
- `geo.geonames_city_id` (*str*): ex. `3078610`
- `geo.region` (*str*): ex. `South Moravian`
- `geo.country_code` (*str*): ex. `CZ`
- `geo.country` (*str*): ex. `Czechia`
- `geo.latitude` (*float*): ex. `49.19522`
- `geo.longitude` (*float*): ex. `16.60796`

## 3. Hierarquia e Relações Institucionais (Chaves de Cruzamento)

- `associated_institutions[]` (*list[dict]*): 1 itens no exemplo
- `associated_institutions[].id` (*str*): ex. `https://openalex.org/I1310815967`
- `associated_institutions[].ror` (*str*): ex. `https://ror.org/01p7k1986`
- `associated_institutions[].display_name` (*str*): ex. `Central European Institute of Technology`
- `associated_institutions[].country_code` (*str*): ex. `CZ`
- `associated_institutions[].type` (*str*): ex. `education`
- `associated_institutions[].relationship` (*str*): ex. `related`
- `lineage[]` (*list[str]*): ex. `https://openalex.org/I4210118976`
- `repositories[]` (*list*): lista vazia neste exemplo
- `roles[]` (*list[dict]*): 1 itens no exemplo
- `roles[].role` (*str*): ex. `institution`
- `roles[].id` (*str*): ex. `https://openalex.org/I4210118976`
- `roles[].works_count` (*int*): ex. `2899`

## 4. Área do Conhecimento e Temática

- `topics[]` (*list[dict]*): 25 itens no exemplo
- `topics[].id` (*str*): ex. `https://openalex.org/T10486`
- `topics[].display_name` (*str*): ex. `Salmonella and Campylobacter epidemiology`
- `topics[].count` (*int*): ex. `279`
- `topics[].score` (*float*): ex. `1.0`
- `topics[].subfield.id` (*str*): ex. `https://openalex.org/subfields/1106`
- `topics[].subfield.display_name` (*str*): ex. `Food Science`
- `topics[].field.id` (*str*): ex. `https://openalex.org/fields/11`
- `topics[].field.display_name` (*str*): ex. `Agricultural and Biological Sciences`
- `topics[].domain.id` (*str*): ex. `https://openalex.org/domains/1`
- `topics[].domain.display_name` (*str*): ex. `Life Sciences`
- `topic_share[]` (*list[dict]*): 25 itens no exemplo
- `topic_share[].id` (*str*): ex. `https://openalex.org/T13791`
- `topic_share[].display_name` (*str*): ex. `Veterinary medicine and infectious diseases`
- `topic_share[].value` (*float*): ex. `0.0033966`
- `topic_share[].subfield.id` (*str*): ex. `https://openalex.org/subfields/3404`
- `topic_share[].subfield.display_name` (*str*): ex. `Small Animals`
- `topic_share[].field.id` (*str*): ex. `https://openalex.org/fields/34`
- `topic_share[].field.display_name` (*str*): ex. `Veterinary`
- `topic_share[].domain.id` (*str*): ex. `https://openalex.org/domains/4`
- `topic_share[].domain.display_name` (*str*): ex. `Health Sciences`

## 5. Métricas de Produção e Impacto

- `works_count` (*int*): ex. `2899`
- `cited_by_count` (*int*): ex. `81404`
- `summary_stats.2yr_mean_citedness` (*float*): ex. `3.3360655737704916`
- `summary_stats.h_index` (*int*): ex. `114`
- `summary_stats.i10_index` (*int*): ex. `1592`
- `counts_by_year[]` (*list[dict]*): 17 itens no exemplo
- `counts_by_year[].year` (*int*): ex. `2026`
- `counts_by_year[].works_count` (*int*): ex. `97`
- `counts_by_year[].oa_works_count` (*int*): ex. `90`
- `counts_by_year[].cited_by_count` (*int*): ex. `5736`
- `works_api_url` (*str*): ex. `https://api.openalex.org/works?filter=institutions.id:I`

## 6. Metadados de Controle

- `is_super_system` (*bool*): ex. `False`
- `created_date` (*str*): ex. `2022-02-02T04:48:36`
- `updated_date` (*str*): ex. `2026-11-20T18:22:16`

## 7. Outros Campos Retornados

- `works_count_with_children` (*int*): ex. `2899`
- `works_count_with_children_and_predecessors` (*int*): ex. `2899`
- `status` (*str*): ex. `active`
- `awards_count` (*int*): ex. `258`
- `awards_api_url` (*str*): ex. `https://api.openalex.org/awards?filter=institution_awar`
