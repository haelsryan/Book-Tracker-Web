# Reading Tracker - Week 2 (clean version)
from models import Series
from logic import getStatus, progressPercent
from storage import load_library, saveLibrary
DATA_FILE = "library.json"
FORMATS = {"1": "Manga", "2": "Novel", "3": "Comic"}


# ========================= ADDONS
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
    for number, series in enumerate(library.items, start=1):
        print(f"{number}. {series} | Last read: {series.last_read or 'never'}")

def addSeries(library):
    title = input("Title: ").strip().title()
    if title == "":
        print("Title can't be empty.")
        return
    if library.has_title(title):
        print("That title is already in your library")
        return
    
    print("Format: 1) Manga  2) Novel  3) Comic")
    fmt = FORMATS.get(input("Pick 1-3: ").strip(), "Unknown")
    total = askInt("Total chapters/pages/issues: ")

    library.add(Series(title, fmt, total))
    print(f"Added {title}!")

def logProgress(library):
    index = askSeriesNumber(library, "Which number? ")
    if index is None:
        return
    amount = askInt("How many to add? ")
    series = library.items[index]
    series.log(amount)
    print(f"Updated {series}")

def removeSeries(library):
    index = askSeriesNumber(library, "Remove which number? ")
    if index is None:
        return
    removed = library.remove(index)
    print(f"Removed {removed['title']}")

def showReading(library):
    print("\nCurrently reading:")
    for series in library.reading():
        print(f"- {series.title}")
    input("\nPress Enter to continue...")

def searchSeries(library):
    results = library.search(input("Search for: ").strip().lower())
    if not results:
        print("No matches.")
    for series in results:
        print(f"- {series.title} [{series.fmt}]")
    input("\nPress Enter to continue...")

def show_stats(library):
    print(f"\nSeries in library: {len(library)}")
    print(f"Currently reading: {len(library.reading())}")
    print(f"Completed: {len(library.completed())}")
    print(f"Manga: {len(library.by_format('Manga'))}")
    print(f"Total chapters/pages/issues read: {library.total_read()}")
    input("\nPress Enter to continue...")

# ==================================================

def main():
    library = load_library()
    print("=== Reading Tracker ===")
    while True:
        showLibrary(library)
        print("\n1) Add  2) Log progress  3) Remove  4) Reading only  5) Search  6) Stats  7) Quit")
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
            show_stats
        elif choice == "7":
           print("Bye!!")
           break
        else:
            print("Not a valid choice.")

        saveLibrary(library)

if __name__ == "__main__":
    main()