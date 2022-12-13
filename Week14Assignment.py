## Chinmay D. 12/7/2022 Hg5590
print('''[1] = Add Book
[2] = Show All Books
[3] = Edit Book
[4] = Remove Book
[exit] = Close Program''')
# Prints a menu with a lists of an action the user can do 
class Library:
# Creates a class with list of output for the Library program
    lib = {}
    def __init__(self): 
        x = input("Please select a number: ")
        if x == '1':
            self.add() 
        elif x == '2':
            self.all()  
        elif x == '3':
            self.edit()  
        elif x == '4':
            self.remove()  
        elif x == 'exit':
            print("Exiting Library..")
# Creates a dictionary to srore book information and sets the values for pickable choices
    def add(self):
        ISBN = int(input("Enter ISBN of book: "))
        if ISBN not in self.lib:
            author = input("Enter author: ")
            price = float(input("Enter price: $"))
            title = input("Enter book's title: ")
            cp = int(input("Enter number of copies purchased: "))
            cnc = int(input("Enter number of copies not checked-out: "))
            self.lib[ISBN] = [author, price, title, cp, cnc]
            self.__init__()
# Checks and validates the availibility of ISBN number
        else:
            print("Error: Pre-existing ISBN")
            self.__init__()
# Creates a function to add book information in the database such as author, price, title, purchased and not checked-out copies

    def all(self):
        for b in self.lib:
            print(
                f"ISBN = {b},author = {self.lib[b][0]}, price = {self.lib[b][1]}, title = {self.lib[b][2]}, copies purchased = {self.lib[b][3]}, copies not checked in = {self.lib[b][4]}")
        self.__init__()
# Creates a function to show all books while assigning values to author, price, title, purchased and not checked-out copies
    def edit(self):
        ISBN = int(input("Enter ISBN #: "))
        x = input('''[author] =  Edit Author
[price] = Edit Price
[title] = Edit Title
[cp] = Edit number of copies purchased 
[cnc] = Edit number of copies not checked-out
Enter a word to continue: ''')
        if x == "author":
            new_author = input("Enter author: ")
            self.lib[ISBN][0] = new_author
        elif x.lower == "price":
            new_price = float(input("Enter price: "))
            self.lib[ISBN][1] = new_price
        elif x.lower == "title":
            new_title = input("Enter book's title: ")
            self.lib[ISBN][2] = new_title
        elif x.lower == "cp":
            new_cp = int(input("Enter number of copies purchased: "))
            self.lib[ISBN][3] = new_cp  
        elif x.lower == "cnc":
            new_cnc = int(input("Enter number of copies not checked-out: "))
            self.lib[ISBN][4] = new_cnc   
        self.__init__()
# Creates a function to edit book information with a new menu to using the ISBN number to navigate
    def remove(self):
        ISBN = int(input("Enter ISBN of book you want to delete: "))
        self.lib.pop(ISBN)
        self.__init__()
# Creates a function to remove the books based of ISBN number
week14 = Library()
# Creates an object for class and runs all functions while using a constructor 