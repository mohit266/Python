# Library Management System
class Library:
    def __init__(self, list_of_books, name):
        self.list_of_books = list_of_books
        self.name = name
        self.lendDict = {}
        self._secret_key = ""

    def display_book(self):
        for index, book in enumerate(self.list_of_books):
            print(f" {index+1}.{book}")

    def lend_book(self, user, book, sec_key):
        self._secret_key = sec_key
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender book database has been updated. You can take the book now.")
        else:
            print(f"Book is already issued by {self.lendDict[book]}")

    def add_book(self, book):
        self.list_of_books.append(book)
        print("Thank you!!! Book has been added to the library.")

    def return_book(self, book, sec_key):
        if self._secret_key == sec_key:
            self.lendDict.pop(book)  # In Dictionary we use pop func
            print(f"Your book is successfully returned")
        else:
            print("Please enter valid key to returned the book")

    def display_lendDict(self):
        for index, book in enumerate(self.lendDict):
            print(f"{index+1}.{book} book is lend by {self.lendDict[book]}")

    def del_book(self, book, sec_key):
        _secret_key = 123456
        if _secret_key == sec_key:
            self.list_of_books.remove(book)  # In list we use remove func to delete any item
            print("You have successfully removed the book from our library")
        else:
            print("Oops!Please enter valid key")

if __name__ == '__main__':
    Mohit = Library(['Python', 'C++', 'C', 'R.S Agrawal', 'Let Us C', 'R.D Sharma', 'HC Verma'],
                    "Mohit Library Management System")

    while True:
        print(f"\nWelcome to {Mohit.name}")
        print("1.To Display Books")
        print("2.To Lend a Book")
        print("3.To Add a Book")
        print("4.To return a Book")
        print("5.To Display lendDict")
        print("6.To Delete or Remove the Book from the library")

        user_choice = int(input("\nEnter your choice :"))

        if user_choice == 1:
            print(f"\n--> Book available in our library are:")
            Mohit.display_book()

        elif user_choice == 2:
            book = input("\nEnter the name of book which you want to lend : ")
            user = input("Enter your name : ")
            sec_key = int(input("Enter a secret key and keep it private : "))
            Mohit.lend_book(user, book, sec_key)

        elif user_choice == 3:
            book = input("\nEnter book name which you want to add in our library : ")
            Mohit.add_book(book)

        elif user_choice == 4:
            book = input("\nEnter the name of book which you want to return : ")
            sec_key = int(input("Enter your secret key:"))
            Mohit.return_book(book, sec_key)

        elif user_choice == 5:
            print(f"\n--> Books in lendDict")
            Mohit.display_lendDict()

        elif user_choice == 6:
            print("\nOnly Library Authority can delete the book. If you are one of them then \n"
                  "You have to enter your secret key below ")
            sec_key = int(input("\nEnter your secret key here:"))
            book = input("Enter the book name which you want to delete:")
            Mohit.del_book(book, sec_key)

        else:
            print("\nEnter a valid input.")

        user_choice2 = ""
        while user_choice2 != "c" and user_choice2 != "q":
            user_choice2 = input("\nEnter q for quit and c for continue :")
            if user_choice2 == 'q':
                exit()

            elif user_choice2 == 'c':
                continue
