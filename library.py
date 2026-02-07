# Library Management System (Simple Beginner Program)

books = []

while True:
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # Add Book
    if choice == "1":
        book_name = input("Enter book name: ")
        books.append(book_name)
        print("Book added successfully!")

    # View Books
    elif choice == "2":
        if len(books) == 0:
            print("No books available in library.")
        else:
            print("\nBooks in Library:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])

    # Search Book
    elif choice == "3":
        search_name = input("Enter book name to search: ")
        if search_name in books:
            print("Book found in library!")
        else:
            print("Book not found!")

    # Remove Book
    elif choice == "4":
        remove_name = input("Enter book name to remove: ")
        if remove_name in books:
            books.remove(remove_name)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    # Exit
    elif choice == "5":
        print("Thank you! Exiting Library Management System.")
        break

    else:
        print("Invalid choice! Please enter between 1 to 5.")

        print("New update")

