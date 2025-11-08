export class APIKeyAuth {
  private apiKey: string;

  constructor(apiKey: string) {
    this.apiKey = apiKey;
  }
  getHeaders(): Record<string, string> {
    return {};
  }
  getKey(): string {
    return this.apiKey;
  }
}
