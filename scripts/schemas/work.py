WORK_CATEGORIES = {
    "1. Identificação e Metadados Básicos": [
        "id", "doi", "ids", "title", "display_name", "publication_year",
        "publication_date", "language", "type", "type_crossref", "indexed_in"
    ],
    "2. Autoria, Instituições e Países (Chaves de Cruzamento)": [
        "authorships", "corresponding_author_ids", "corresponding_institution_ids",
        "countries_distinct_count", "institutions_distinct_count"
    ],
    "3. Área do Conhecimento e Temática": [
        "primary_topic", "topics", "keywords", "concepts", "mesh",
        "sustainable_development_goals"
    ],
    "4. Periódico, Localização e Acesso Aberto": [
        "primary_location", "locations", "locations_count", "best_oa_location",
        "open_access", "biblio", "apc_list", "apc_paid", "has_fulltext", "fulltext_origin"
    ],
    "5. Métricas de Impacto, Citações e Financiamento": [
        "cited_by_count", "cited_by_api_url", "counts_by_year", "fwci",
        "citation_normalized_percentile", "cited_by_percentile_year",
        "referenced_works", "referenced_works_count", "related_works", "grants", "funders"
    ],
    "6. Resumo e Metadados de Controle": [
        "abstract_inverted_index", "is_retracted", "is_paratext",
        "created_date", "updated_date", "datasets", "versions"
    ]
}