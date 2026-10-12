# Reading Tracker - Week 2 (clean version)
import json
DATA_FILE = "library.json"

# ==================== ADDONS TO HELP PROGRAMS
def getStatus(read, total):
    if read == 0:
        return "Plan to Read"
    elif read >= total:
        return "Completed"

def progressPercent(read, total):
    return round(read / total * 100, 1)

def askInt(prompt, minimum = 1):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please type a whole number.")
            continue
        if value < minimum:
            print(f"Must be at least {minimum}.")
            continue
        return value

def askSeriesNumber(library, prompt):
    number = askInt(prompt)
    if not 1 <= number <= len(library):
        print("No series with that number")
        return None
    return number - 1
# =======================================

# ==================== MENU FUNCTION
def showLibrary(library):
    print()
    if not library:
        print("(Library is empty)")
    for number, series in enumerate(library, start=1):
        percent = progressPercent(series["read"], series["total"])
        status = getStatus(series["read"], series["total"])
        print(f"{number}. {series['title']} [{series['fmt']}] "f"{series['read']}/{series['total']} ({percent}%) - {status}")

def addSeries(library):
    title = input("Title: ").strip().title()
    if title == "":
        print("Title can't be empty.")
        return
    print("Format: 1) Manga  2) Novel  3) Comic")
    fmt = FORMATS.get(input("Pick 1-3: ").strip(), "Unknown")
    total = askInt("Total chapters/pages/issues: ")
    library.append({"title": title, "fmt": fmt, "read": 0, "total": total})
    print(f"Added {title}!")

def logProgress(library):
    index = askSeriesNumber(library, "Which number? ")
    if index is None:
        return
    amount = askInt("How many to add? ")
    series = library[index]
    series["read"] = min(series["read"] + amount, series["total"])
    print(f"Updated {series['title']}: {series['read']}/{series['total']}")

def removeSeries(library):
    index = askSeriesNumber(library, "Remove which number? ")
    if index is None:
        return
    removed = library.pop(index)
    print(f"Removed {removed['title']}")


def showReading(library):
    print("\nCurrently reading:")
    for series in library:
        if 0 < series["read"] < series["total"]:
            print(f"- {series['title']}")
    input("\nPress Enter to continue...")

def searchSeries(library):
    word = input("Search for: ").strip().lower()
    found = False
    for series in library:
        if word in series["title"].lower():
            print(f"- {series['title']} [{series['fmt']}]")
            found = True
    if not found:
        print("No matches.")
    input("\nPress Enter to continue...")
# ==================================================

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
FORMATS = {"1": "Manga", "2": "Novel", "3": "Comic"}

def main():
    library = [
        {"title": "Vagabond", "fmt": "Manga", "read": 12, "total": 327},
        {"title": "Dune", "fmt": "Novel", "read": 100, "total": 600},
    ]
    print("=== Reading Tracker ===")
    while True:
        showLibrary(library)
        print("\n1) Add  2) Log progress  3) Remove  4) Reading only  5) Search  6) Quit")
        choice = input("> ").strip()

        if choice == "1":
            addSeries(library)
        elif choice == "2":
            logProgress(library)
        elif choice == "3":
            removeSeries(library)
        elif choice == "4":
            showReading(library)
        elif choice == "5":
            searchSeries(library)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Not a valid choice.")
        saveLibrary(library)

main()