class library :
    def __init__(self,list_of_books,name):
        self.booklist=list_of_books
        self.name=name
        self.lendingdictionary={}
    

    def displayBook(self):
        print(f"We have the following books in the library : {self.name}")
        for book in self.booklist:
            print(book)

    
    def lendingBook(self,user,book):
        if book not in self.booklist:
            print("sorry we don't have this book")
        elif book in self.lendingdictionary:
            print(f"the book is already been used by :{self.lendingdictionary[book]}")
        else:
            self.lendingdictionary[book]= user
            print("lending boook data base has been updated,you can take the book now")


    def addBook(self,book):
        self.booklist.append(book)
        print(f"{book} has been added to the book list")


    def returnBook(self,book):
        if book in self.lendingdictionary:
            del self.lendingdictionary[book]
            print("Book has been returned")
        else:
            print("The book wasn't been borrowed by us")



listOfBooks = ["python","rich dad poor dad","harry potter","C++ basic","algorithims"]

books=library(listOfBooks,"upskill")

userName = input("welcome to our library,please enter your name : ")

while True:
    print(f"\n hello {userName} , welcome to the {books.name} library. Please choose an option")
    print("1. Display books \n 2. Lend a book \n 3. Add a book \n 4. Return a book \n 5.Quit")
    userchoice = input("enter your choice to continue : ")


    if userchoice == "1":
        books.displayBook()
    elif userchoice == "2":
        book = input("enter the name of a book, you want to lend : ")
        books.lendingBook(userName,book)
    elif userchoice == "3":
        book = input("enter the name of the book which you want to add : ")
        books.addBook(book)
    elif userchoice == "4":
        book = input("enter the name of the book which you want to return : ")
        books.returnBook(book)
    elif userchoice == "5":
        print(f"Thank you for using the library {userName} . Goodbye!")
        break 
    else:
        print("Enter the valid input")
