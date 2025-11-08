# Google Custom Search API Python SDK

## Usage
```python
from google_custom_search_api import GoogleCustomSearchClient
client = GoogleCustomSearchClient(api_key="YOUR_KEY")
results = client.cse_list(q="hello world", cx="engine_id")
print(results.items)
```
- All endpoints and parameters are covered according to the OpenAPI documentation.
- See models.py for complete data structures.
