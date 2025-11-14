import requests
from urllib.parse import urljoin

def create_elementor_page(wp_site_url, username, app_password, title, data):
    api = urljoin(wp_site_url, "/wp-json/wp/v2/")
    auth = (username, app_password)

    # Create page
    r = requests.post(
        api + "pages",
        auth=auth,
        json={"title": title, "status": "publish"},
    )
    r.raise_for_status()
    page = r.json()
    page_id = page["id"]

    # Update meta with Elementor
    r = requests.post(
        api + f"pages/{page_id}",
        auth=auth,
        json={
            "meta": {
                "_elementor_edit_mode": "builder",
                "_elementor_template_type": "wp-page",
                "_elementor_data": data
            }
        }
    )
    r.raise_for_status()

    return page["link"]
