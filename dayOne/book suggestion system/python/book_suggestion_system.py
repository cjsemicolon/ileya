import random

books = [
    "Harry Potter",
    "Fourth Wing",
    "The Chronicles Of Narnia",
    "Percy Jackson",
    "A Song of Ice and Fire",
]

def get_book_suggestions():
    random_book = random.choice(books)
    return random_book

def get_page_suggestions():
    random_page = random.randint(1, 100)
    return random_page

def add_book(new_book):
    for book in books:
        if book == new_book:
            return "Book already exists"
    books.append(new_book)
    return "Book added successfully"

def remove_book(delete_book):
    for book in books:
        if book == delete_book:
            books.remove(delete_book)
            return "Book removed successfully"
    return "Book not found"

def update_book(old_book_title, new_book_title):
    for book in books:
        if book == old_book_title:
            new_title = new_book_title
            index = books.index(old_book_title)
            books[index] = new_title
            return "Book updated successfully"
    return "Book not found"

def show_all_books(books):
    print(books)


def menu():
    while True:
        print("""
                    WELCOME TO THE BOOK SUGGESTION APP
1. Get Suggestions
2. Add Book
3. Remove Book
4. UpdateBook
5. Show all books
6. Exit
              """  )
        choice = int(input("Select a choice: "))
        
        if choice == 1:
            print("Book: ", get_book_suggestions())
            print("page: ", get_page_suggestions())

        elif choice == 2:
            print(add_book(new_book = input("Enter new book name: ")))

        elif choice == 3:
            print(remove_book(delete_book = input("Enter book to delete: ")))

        elif choice == 4:
            old_book_title = input("Enter book to update: ")
            new_book_title = input("Enter updated book title: ")
            print(update_book(old_book_title, new_book_title))

        elif choice == 5:
            print(books)

        elif choice == 6:
            print("Goodbye!")
            break
menu()








 
