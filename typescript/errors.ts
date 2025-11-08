export class GoogleCustomSearchAPIError extends Error {
  constructor(message: string) {
    super(message);
    this.name = 'GoogleCustomSearchAPIError';
  }
}
