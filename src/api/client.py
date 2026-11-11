import requests
from typing import Dict, Any, Optional

class OpenAlexClient:
    def __init__(self, email: str):
        self.base_url = "https://api.openalex.org"
        self.email = email
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": f"LatAMReserchExplorer/1.0 (mailto:{self.email})"
        })

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        if params is None:
            params = {}

        params["mailto"] = self.email

        try:
            response = self.session.get(url, params=params, timeout=12)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            print(f"[ERRO HTTP] Status {response.status_code} em {url}: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            print(f"[ERRO CONEXÃO] Falha ao conectar com {url}: {req_err}")
            raise