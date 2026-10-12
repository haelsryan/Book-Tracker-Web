# Reading Tracker - Week 2 (clean version)

FORMATS = {"1": "Manga", "2": "Novel", "3": "Comic"}

library = [
    {"title": "Vagabond", "fmt": "Manga", "read": 12, "total": 327},
    {"title": "Dune", "fmt": "Novel", "read": 100, "total": 600},
]

print("=== Reading Tracker ===")

while True:
    # ---------- Show library ----------
    print()
    if not library:
        print("(library is empty)")

    for number, series in enumerate(library, start=1):
        percent = round(series["read"] / series["total"] * 100, 1)

        if series["read"] == 0:
            status = "Plan to Read"
        elif series["read"] >= series["total"]:
            status = "Completed"
        else:
            status = "Reading"

        print(f"{number}. {series['title']} [{series['fmt']}] "
              f"{series['read']}/{series['total']} ({percent}%) - {status}")

    # ---------- Menu ----------
    print("\n1) Add  2) Log progress  3) Remove  4) Reading only  5) Search  6) Quit")
    choice = input("> ").strip()

    # ---------- 1) Add ----------
    if choice == "1":
        title = input("Title: ").strip().title()
        if title == "":
            print("Title can't be empty.")
            continue

        print("Format: 1) Manga  2) Novel  3) Comic")
        fmt = FORMATS.get(input("Pick 1-3: ").strip(), "Unknown")

        try:
            total = int(input("Total chapters/pages/issues: "))
        except ValueError:
            print("Please type a whole number.")
            continue

        if total < 1:
            print("Total must be at least 1.")
            continue

        library.append({"title": title, "fmt": fmt, "read": 0, "total": total})
        print(f"Added {title}!")

    # ---------- 2) Log progress ----------
    elif choice == "2":
        try:
            number = int(input("Which number? "))
            amount = int(input("How many to add? "))
        except ValueError:
            print("Please type whole numbers.")
            continue

        if not 1 <= number <= len(library):
            print("No series with that number.")
            continue
        if amount < 1:
            print("Amount must be at least 1.")
            continue

        series = library[number - 1]
        series["read"] = min(series["read"] + amount, series["total"])
        print(f"Updated {series['title']}: {series['read']}/{series['total']}")

    # ---------- 3) Remove ----------
    elif choice == "3":
        try:
            number = int(input("Remove which number? "))
        except ValueError:
            print("Please type a whole number.")
            continue

        if not 1 <= number <= len(library):
            print("No series with that number.")
            continue

        removed = library.pop(number - 1)
        print(f"Removed {removed['title']}")

    # ---------- 4) Reading only ----------
    elif choice == "4":
        print("\nCurrently reading:")
        for series in library:
            if 0 < series["read"] < series["total"]:
                print(f"- {series['title']}")
        input("\nPress Enter to continue...")

    # ---------- 5) Search ----------
    elif choice == "5":
        word = input("Search for: ").strip().lower()
        found = False
        for series in library:
            if word in series["title"].lower():
                print(f"- {series['title']} [{series['fmt']}]")
                found = True
        if not found:
            print("No matches.")
        input("\nPress Enter to continue...")

    # ---------- 6) Quit ----------
    elif choice == "6":
        print("Bye!")
        break

    else:
        print("Not a valid choice.")