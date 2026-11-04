class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def describe(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} | {self.author} | {status}"
