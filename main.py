The_books = {"Harry Potter and the philosopher's stone":9780439203524,
             "Harry Potter and the chamber of secrets":8580001045948,
             "Harry Potter and the Prisoner of Azkaban":9780747542155,
             "Harry Potter and the goblet of fire":9781408845677,
             "Harry Potter and the order of the phoenix":9780439567619}

borrowed_books = {}

def menu_print():
    print("press l to show the library")
    print("press a to add a book")
    print("press c to change the information of a book")
    print("press d to delete a book")
    print("press b to borrow a book")
    print("press r to return a book")
    print("press q to quit")

def show_things(The_books):
    print()
    for key in The_books:
        print(key, ' : ', The_books[key])
    print()

def add_things(The_books):
    add_what = input("Which book do you want to add? ")
    ISBN = input("And what is the ISBN number of this book? ")
    The_books[add_what] = ISBN

def change_things(The_books, borrowed_books):
    change_information = input("From which book do you want to change the information? ")
    if change_information not in The_books and not borrowed_books:
        print()
        print("We do not have that book, sorry!")
        print()

    elif change_information in borrowed_books and not The_books:
        print()
        print("We can't change the information of books that have been borrowed, sorry!")
        print()
    else:
        T_of_I = input("Do you want to change the Title, The ISBN number or both?  ")
        if T_of_I == "title":
            wat_wel_Title = input("Wat does the Title need to be called? ")
            The_books[wat_wel_Title] = The_books.pop(change_information)

        elif T_of_I == "ISBN":
            wat_wel_ISBN = input("Wat does need to be the ISBN number? ")
            The_books[change_information] = wat_wel_ISBN

        elif T_of_I == "both":
            wat_wel_Title = input("Wat does the Title need to be called? ")
            wat_wel_ISBN = input("Wat does need to be the ISBN number? ")
            The_books[wat_wel_Title] = The_books.pop(change_information)
            The_books[wat_wel_Title] = wat_wel_ISBN

        else:
            print("No Capital letters! in title or both, however there are Capitol letters in ISBN!")

def delete_things(The_books, borrowed_books):
    delete_what = input("which book do you want to delete? ")
    if delete_what in The_books:
        print()
        The_books.pop(delete_what)
        print("Your book has been deleted!")
        print()
    elif delete_what in borrowed_books:
        print()
        borrowed_books.pop(delete_what)
        print("Your book has been deleted!")
        print()
    else:
        print()
        print("We do not have that book!")
        print()

def borrow_things(The_books, borrowed_books):
    borrow_book = input("What book do you wish to borrow? ")
    if borrow_book in The_books:
        borrowed_books[borrow_book] = The_books.pop(borrow_book)
        print()
        print(borrow_book + "has been borrowed successfully")
        print()
    elif borrow_book in borrowed_books:
        print()
        print("This book has already been taken.")
        print()
    else:
        print()
        print("Sorry, we do not have that book.")
        print()

def return_things(The_books, borrowed_books):
    return_what = input("What book do you wish to return? ")
    if return_what in The_books:
        print()
        print("That book has already been returned!")

    elif return_what in borrowed_books:
        print()
        The_books[return_what] = borrowed_books.pop(return_what)
        print("The Book: " + return_what + "has been successfully returned!")
        print()

    else:
        print()
        print("We do not have that book in our collection!")
        print()

def main(The_books, borrowed_books):
    on = True
    while on:
        menu_print()
        Awnser = input("Your awnser: ")
        if Awnser == "l":
           show_things(The_books)

        elif Awnser == "a":
            add_things(The_books)

        elif Awnser == "c":
            change_things(The_books, borrowed_books)

        elif Awnser == "d":
            delete_things(The_books, borrowed_books)

        elif Awnser == "b":
            borrow_things(The_books, borrowed_books)

        elif Awnser == "r":
            return_things(The_books, borrowed_books)

        elif Awnser == "q":
            on = False

main(The_books, borrowed_books)