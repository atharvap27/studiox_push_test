from typing import Dict

class APIKeyAuth:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_headers(self) -> Dict[str, str]:
        return {}

    def get_query_params(self) -> Dict[str, str]:
        return {"key": self.api_key}
