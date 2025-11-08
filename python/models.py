from typing import List, Optional, Dict
from pydantic import BaseModel
from enum import Enum

class SafeLevel(str, Enum):
    high = 'high'
    medium = 'medium'
    off = 'off'

class SearchType(str, Enum):
    image = 'image'

class Context(BaseModel):
    title: Optional[str]

class QueryInfo(BaseModel):
    title: Optional[str]
    totalResults: Optional[str]
    searchTerms: Optional[str]
    count: Optional[int] = None
    startIndex: Optional[int] = None
    inputEncoding: Optional[str]
    outputEncoding: Optional[str]
    safe: Optional[str]
    cx: Optional[str]

class Promotion(BaseModel):
    title: Optional[str]
    link: Optional[str]
    bodyLines: Optional[List[Dict[str, str]]]

class SearchInformation(BaseModel):
    searchTime: Optional[float]
    formattedSearchTime: Optional[str]
    totalResults: Optional[str]
    formattedTotalResults: Optional[str]

class Result(BaseModel):
    kind: Optional[str]
    title: Optional[str]
    htmlTitle: Optional[str]
    link: Optional[str]
    displayLink: Optional[str]
    snippet: Optional[str]
    htmlSnippet: Optional[str]
    cacheId: Optional[str]
    mime: Optional[str]
    fileFormat: Optional[str]
    image: Optional[Dict[str, str]]

class SearchResponse(BaseModel):
    kind: Optional[str]
    url: Optional[Dict[str, str]]
    queries: Optional[Dict[str, List[QueryInfo]]]
    context: Optional[Context]
    searchInformation: Optional[SearchInformation]
    items: Optional[List[Result]]
    promotions: Optional[List[Promotion]]
