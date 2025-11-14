from models import PageStructure, SectionData

def section_to_elementor(section: SectionData, i: int):
    return {
        "id": f"section_{i}",
        "elType": "section",
        "elements": [
            {
                "id": f"column_{i}_1",
                "elType": "column",
                "settings": {"_column_size": 100},
                "elements": [
                    {
                        "id": f"widget_{i}_1",
                        "elType": "widget",
                        "widgetType": "text-editor",
                        "settings": {"editor": section.html},
                        "elements": []
                    }
                ]
            }
        ],
        "settings": {}
    }

def build_elementor_data(page: PageStructure):
    return [section_to_elementor(sec, i) for i, sec in enumerate(page.sections)]
