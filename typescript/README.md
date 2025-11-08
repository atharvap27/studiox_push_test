# Google Custom Search API TypeScript SDK

## Usage
```typescript
import { GoogleCustomSearchClient } from './client';
const client = new GoogleCustomSearchClient('YOUR_API_KEY');
client.cseList({q: 'hello world', cx: 'engine_id'}).then(r => {
  console.log(r.items);
});
```
- All endpoints and parameters are covered per OpenAPI spec.
- See models.ts for complete data structures.
