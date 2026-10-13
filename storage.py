import json
from models import Library, Series

DATA_FILE = "library.json"

# ========== SAVING AND LOADING JSON FILE
def saveLibrary(library):
    data = [series.to_dict() for series in library.items]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def load_library():
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return Library()          # not []
    except json.JSONDecodeError:
        print("library.json is damaged. Starting empty.")
        return Library()          # not []

    return Library([Series(**item) for item in data]) 
# ==========================================