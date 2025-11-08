import axios, { AxiosInstance } from 'axios';
import { SearchResponse } from './models';
import { APIKeyAuth } from './auth';
import { GoogleCustomSearchAPIError } from './errors';

export class GoogleCustomSearchClient {
  private baseUrl: string;
  private axios: AxiosInstance;
  private auth: APIKeyAuth;

  constructor(apiKey: string, baseUrl: string = 'https://www.googleapis.com') {
    this.baseUrl = baseUrl.replace(/\/$/, '');
    this.axios = axios.create();
    this.auth = new APIKeyAuth(apiKey);
  }

  async cseList(params: {
    q: string;
    cx: string;
    safe?: 'off'|'medium'|'high';
    lr?: string;
    num?: number;
    start?: number;
    sort?: string;
    filter?: string;
    gl?: string;
    cr?: string;
    siteSearch?: string;
    siteSearchFilter?: string;
    exactTerms?: string;
    excludeTerms?: string;
    linkSite?: string;
    orTerms?: string;
    relatedSite?: string;
    dateRestrict?: string;
    searchType?: 'image';
    fields?: string;
    imgSize?: string;
    imgType?: string;
    imgColorType?: string;
    imgDominantColor?: string;
    alt?: string;
  }): Promise<SearchResponse> {
    try {
      const res = await this.axios.get<SearchResponse>(
        `${this.baseUrl}/customsearch/v1`,
        {
          params: { ...params, key: this.auth.getKey() },
          headers: this.auth.getHeaders(),
        }
      );
      return res.data;
    } catch (e) {
      throw new GoogleCustomSearchAPIError((e as Error).message);
    }
  }
}
