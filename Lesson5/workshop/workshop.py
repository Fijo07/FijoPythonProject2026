# dhow all books
# add new book
# borwwo,
# return
# quit
from Lesson5.workshop.book import Book


def add_book(books, title, author):
    new_book = Book(title, author)
    books.append(new_book)
    print(f"added new book: {title} - {author}")


def display_books(books):
    if not books:
        print("no books")
    else:
        for i, book in enumerate(books, 1):
            print(f"{i}. {book.describe()}")


def borrow_book(books, book_number):
    if 0 < book_number <= len(books):
        book = books[book_number-1]
        if book.available:
            book.available = False
            print(f"you borrowed book: {book.title}")
        else:
            print("book is already bowwored")
    else:
        print("book not exists")


def return_book(books, book_number):
    if 0 < book_number <= len(books):
        book = books[book_number - 1]
        if not book.available:
            book.available = True
            print(f"you returned book: {book.title}")
        else:
            print("book is already available")
    else:
        print("book not exists")


if __name__ == "__main__":


    books = []



    while True:
        print("\n---Menu---\n")
        print("1. Show all book")
        print("2. add new book")
        print("3. borrow a book")
        print("4. return a book")
        print("5. quit")

        choice = input("choose the option:")

        if choice == "1":
            display_books(books)


        elif choice == "2":
            title = input("enter the book title:")
            author = input("enter the book author:")
            add_book(books, title, author)

        elif choice == "3":
            display_books(books)
            try:
                book_number = int(input("enter the book number:"))
                borrow_book(books, book_number)
            except ValueError:
                print("Please enter a correct number")

        elif choice == "4":
            display_books(books)
            try:
                book_number = int(input("enter the book number:"))
                return_book(books, book_number)
            except ValueError:
                print("Please enter a correct number")


        elif choice == "5":
            print("Thank you for your time")
            break
        else:
            print("Please choose a valid option")
