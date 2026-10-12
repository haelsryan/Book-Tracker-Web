import json

DATA_FILE = "library.json"

# ========== SAVING AND LOADING JSON FILE
def saveLibrary(library):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(library, f, indent=2, ensure_ascii=False)

def loadLibrary(library):
    try:
        with open(DATA_FILE, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("library.json is Damaged Starting empty.")
        return []
# ==========================================