print("=== Reading Tracker ===")
title = input("Series title: ").strip().title()

print("Format: 1) Manga  2) Novel  3) Comic")
choice = input("Pick 1-3: ")
if choice == "1":
    fmt, unit = "Manga", "chapters"
elif choice == "2":
    fmt, unit = "Novel", "pages"
elif choice == "3":
    fmt, unit = "Comic", "issues"
else:
    fmt, unit = "Unknown", "items"

read = int(input(f"{unit.title()} read: "))
total = int(input(f"Total {unit}: "))
progress = round(read / total * 100, 1)

if read == 0:
    status = "Plan to Read"
elif read >= total:
    status = "Completed"
else:
    status = "Reading"

print(f"\n{title} [{fmt}]")
print(f"{read}/{total} {unit} ({progress}%) - {status}")