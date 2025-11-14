import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from models import PageStructure, SectionData

def scrape_page(url: str) -> PageStructure:
    resp = requests.get(url, timeout=20)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    title = soup.title.text if soup.title else "Cloned Page"
    sections = []

    for sec in soup.find_all(["section", "div"], recursive=True):
        text = sec.get_text(" ", strip=True)
        if not text or len(text) < 40:
            continue

        images = [
            urljoin(url, img["src"])
            for img in sec.find_all("img")
            if img.get("src")
        ]

        sections.append(
            SectionData(
                html=str(sec),
                text=text,
                images=images
            )
        )
        if len(sections) >= 12:
            break

    if not sections:
        body = soup.body or soup
        text = body.get_text(" ", strip=True)
        images = [urljoin(url, img["src"]) for img in body.find_all("img")]
        sections.append(SectionData(html=str(body), text=text, images=images))

    return PageStructure(title=title, sections=sections)
