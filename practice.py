s = {"title": "Vagabond", "fmt": "Manga", "read": 12, "total": 327}
s["read"] += 1
s["rating"] = 9
print(s.get("notes", "no notes"))
for key, value in s.items():
    print(key, "=", value)
formats = {"1": "Manga", "2": "Novel", "3": "Comic"}
print(formats.get("2", "Unknown"))