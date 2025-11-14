from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from config import settings
from models import CloneRequest, CloneResponse
from scraper import scrape_page
from elementor_builder import build_elementor_data
from wp_client import create_elementor_page

app = FastAPI(title="Rea AutoCloner API", version="0.1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/health")
def health():
    return {"status": "OK"}

@app.post("/api/clone")
def clone(req: CloneRequest):
    try:
        page = scrape_page(str(req.url))
        elementor_data = build_elementor_data(page)

        wp_url = None
        if req.wp_site_url and req.wp_username and req.wp_app_password:
            wp_url = create_elementor_page(
                str(req.wp_site_url),
                req.wp_username,
                req.wp_app_password,
                page.title,
                elementor_data,
            )

        return CloneResponse(
            success=True,
            message="Page cloned successfully",
            source_url=req.url,
            title=page.title,
            elementor_data=elementor_data,
            wp_page_url=wp_url,
        )
    except Exception as e:
        raise HTTPException(500, f"Error: {e}")
