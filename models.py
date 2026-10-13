from datetime import date

# CLASS FOR HANDLING ONE TITLE (MANGA, NOVEL, OR COMIC) ===================
class Series:
    def __init__(self, title, fmt, total, read=0, last_read=None):
        self.title = title
        self.fmt = fmt
        self.total = total
        self.read = read
        self.last_read = last_read

    def progress(self):
        if self.total == 0:
            return 0.0
        return round(self.read / self.total * 100, 1)

    def status(self):
        if self.read == 0:
            return "Plan to Read"
        elif self.read >= self.total:
            return "Completed"
        return "Reading"

    def log(self, amount):
        self.read = min(self.read + amount, self.total)
        self.last_read = date.today().isoformat()

    def to_dict(self):
        return {
            "title": self.title,
            "fmt": self.fmt,
            "total": self.total,
            "read": self.read,
            "last_read": self.last_read
        }

    def __str__(self):
        return (f"{self.title} [{self.fmt}] {self.read}/{self.total}" f"({self.progress()}%) - {self.status()}")



# THE WHOLE BOOKSELF: A LIST OF SERIES + ACTION ===============
class Library:
    def __init__(self, items=None):
        self.items = items or []

    def add(self, series):
        self.items.append(series)

    def remove(self, index):
        return self.items.pop(index)

    def has_title(self, title):
        for series in self.items:
            if series.title.lower() == title.lower():
                return True
        return False

    def search(self, word):
        return [s for s in self.items if word.lower() in s.title.lower()]

    def reading(self):
        return [s for s in self.items if s.status() == "Reading"]
    
    def completed(self):
        return [s for s in self.items if s.status() == "Completed"]

    def by_format(self, fmt):
        return [s for s in self.items if s.fmt.lower() == fmt.lower()]

    def total_read(self):
        total = 0
        for series in self.items:
            total += series.read
        return total

    def __len__(self):
        return len(self.items)