export interface Context {
  title?: string;
}

export interface QueryInfo {
  title?: string;
  totalResults?: string;
  searchTerms?: string;
  count?: number;
  startIndex?: number;
  inputEncoding?: string;
  outputEncoding?: string;
  safe?: string;
  cx?: string;
}

export interface Promotion {
  title?: string;
  link?: string;
  bodyLines?: Array<Record<string, string>>;
}

export interface SearchInformation {
  searchTime?: number;
  formattedSearchTime?: string;
  totalResults?: string;
  formattedTotalResults?: string;
}

export interface Result {
  kind?: string;
  title?: string;
  htmlTitle?: string;
  link?: string;
  displayLink?: string;
  snippet?: string;
  htmlSnippet?: string;
  cacheId?: string;
  mime?: string;
  fileFormat?: string;
  image?: Record<string, string>;
}

export interface SearchResponse {
  kind?: string;
  url?: Record<string, string>;
  queries?: Record<string, QueryInfo[]>;
  context?: Context;
  searchInformation?: SearchInformation;
  items?: Result[];
  promotions?: Promotion[];
}

export type SafeLevel = 'off' | 'medium' | 'high';
export type SearchType = 'image';
