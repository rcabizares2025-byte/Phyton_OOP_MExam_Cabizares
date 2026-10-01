class ReadingList:
    def __init__(self):
        self._books = []

    def add_book(self, title):
        if not title.strip():
            raise ValueError
        self._books.append(title)

    def count(self):
        return len(self._books)

    def titles(self):
        return self._books.copy()


personal = ReadingList()
team = ReadingList()

personal.add_book("Python Basics")
personal.add_book("OOP")
team.add_book("Testing")

external = personal.titles()
external.append("Outside")

print(personal.count())
print(team.count())