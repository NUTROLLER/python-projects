
class Library:

    def __init__(self, book_list, lib_name):
        self.book_list = book_list
        self.lib_name = lib_name
        print(f"Welcome to {self.lib_name}'s Library!")
        self.lended_book = {}

    def Displaybooks(self):
        print("Available books:")
        if not self.book_list:
            print("Sorry! There are no books available at the moment.")
        else:
            for idx, book_name in enumerate(self.book_list,1):
                print(f"{idx}: {book_name}")

    def Lendbook(self, book_idx, borrower):
        #Check if the index even belongs or not:
        if (book_idx > len(self.book_list)):
            print("Uh oh, we don't have that book. Try something else.")
        else:
            self.lended_book.update({self.book_list[book_idx-1]: borrower})
            print(f"Lended '{self.book_list[book_idx-1]}' to {borrower}")
            self.book_list.pop(book_idx-1)

    def Addbook(self, book_name):
        print("Thank you for your contribution! Your book has been added.")
        self.book_list.append(book_name)

    def Returnbook(self):
        if not self.lended_book: #Pythonic way to check if a list is empty...
            print("You have currently not lended any books. Try lending some!")
        else:
            print("Currently, you have lended these book(s):")
            for idx, book_name in enumerate(self.lended_book,1):
                print(f"{idx}: {book_name}")
            try:
                return_index = int(input("Which book would you like to return?:"))
                #Add the book back
                if return_index in range(1,(len(self.lended_book)+1)):
                    list_of_lended_books = list(self.lended_book.keys())
                    self.book_list.append(list_of_lended_books[return_index-1])
            #Remove the book from lended books
            #As it is a dictionary now, we'll first convert it into a list, access key to delete
            #then delete it using del dict[key_to_remove]
                    keys_list = list(self.lended_book)
                    index_to_remove = return_index - 1
                    key_to_remove = keys_list[index_to_remove]
                    del self.lended_book[key_to_remove]
                    print("Thank you for returning the book.")
                else:
                    print(f"Please select within {range(1,len(self.lended_book)+1)}.")
            except ValueError:
                    print("Invalid selection. Please enter a valid number.")

lib1 = Library(["The Hunger Games", "Harry Potter", "To Kill A Mockingbird", "Pride and Prejudice", "Chanakya Neeti", "Mahabharata"], "Akshat")
lib1.Displaybooks()
lib1.Addbook("The Three Mistakes of My Life")
lib1.Displaybooks()
lib1.Lendbook(7, "Vishal")
lib1.Displaybooks()
lib1.Returnbook()
lib1.Displaybooks()
    