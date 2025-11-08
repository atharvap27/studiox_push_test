import requests
from typing import Optional, List, Dict, Any
from .models import SearchResponse
from .auth import APIKeyAuth
from .errors import GoogleCustomSearchAPIError

class GoogleCustomSearchClient:
    def __init__(self, api_key: str, base_url: str = 'https://www.googleapis.com'):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        self.auth = APIKeyAuth(api_key)

    def cse_list(self, q: str, cx: str, safe: Optional[str] = None, lr: Optional[str] = None, num: Optional[int] = None,
                 start: Optional[int] = None, sort: Optional[str] = None, filter: Optional[str] = None,
                 gl: Optional[str] = None, cr: Optional[str] = None, siteSearch: Optional[str] = None,
                 siteSearchFilter: Optional[str] = None, exactTerms: Optional[str] = None,
                 excludeTerms: Optional[str] = None, linkSite: Optional[str] = None, orTerms: Optional[str] = None,
                 relatedSite: Optional[str] = None, dateRestrict: Optional[str] = None,
                 searchType: Optional[str] = None, fields: Optional[str] = None, imgSize: Optional[str] = None,
                 imgType: Optional[str] = None, imgColorType: Optional[str] = None,
                 imgDominantColor: Optional[str] = None, alt: Optional[str] = None) -> SearchResponse:
        """
        Performs a Google Custom Search query.
        https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
        """
        url = f"{self.base_url}/customsearch/v1"
        params = {"q": q, "cx": cx}
        optional_params = [
            'safe', 'lr', 'num', 'start', 'sort', 'filter', 'gl', 'cr', 'siteSearch',
            'siteSearchFilter', 'exactTerms', 'excludeTerms', 'linkSite', 'orTerms', 'relatedSite',
            'dateRestrict', 'searchType', 'fields', 'imgSize', 'imgType', 'imgColorType', 'imgDominantColor', 'alt'
        ]
        for param in optional_params:
            value = locals()[param]
            if value is not None:
                params[param] = value
        headers = self.auth.get_headers()
        params.update(self.auth.get_query_params())
        try:
            resp = self.session.get(url, headers=headers, params=params)
            resp.raise_for_status()
            return SearchResponse.parse_obj(resp.json())
        except requests.RequestException as e:
            raise GoogleCustomSearchAPIError(str(e))
