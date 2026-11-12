from src.config import LATAM_COUNTRIES

def show_latam_codes():
    print("\n--- CODIGOS ISO (AMERICA LATINA) ---")
    for code, country in LATAM_COUNTRIES.items():
        print(f"  {code} -> {country}")
    print("-----------------")