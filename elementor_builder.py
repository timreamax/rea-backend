from models import SectionData, PageStructure


def section_to_elementor(section: SectionData, idx: int):
    return {
        "id": f"section_{idx}",
        "elType": "section",
        "elements": [
            {
                "id": f"column_{idx}_1",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": f"widget_{idx}_1",
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {"editor": section.html},
                        "elements": [],
                    }
                ],
            }
        ],
        "settings": {},
    }


def build_elementor_data(page: PageStructure):
    return [section_to_elementor(sec, i) for i, sec in enumerate(page.sections)]
