from pydantic import BaseModel, HttpUrl
from typing import List, Optional, Any

class SectionData(BaseModel):
    html: str
    text: str
    images: List[str]

class PageStructure(BaseModel):
    title: str
    sections: List[SectionData]

class CloneRequest(BaseModel):
    url: HttpUrl
    wp_site_url: Optional[HttpUrl] = None
    wp_username: Optional[str] = None
    wp_app_password: Optional[str] = None

class CloneResponse(BaseModel):
    success: bool
    message: str
    source_url: HttpUrl
    title: str
    elementor_data: list
    wp_page_url: Optional[str]
