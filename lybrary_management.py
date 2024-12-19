
from library import Library

##classes
class Book:
    def __init__(self,book_id,book_name,author,is_available=True):
        self.book_id = book_id
        self.book_name = book_name
        self.author = author
        self.is_available = is_available

    


class Member:
    def __init__(self,regi_number,name,dob):
        self.regi_number = regi_number
        self.name = name
        self.dob = dob
        self.borrowed_books = []

class Login:
    def __init__(self,username,password):
        self.username = username
        self.password = password


username1 = "user"
password1 = "123"
username = ""
password = ""

##lists
members = []
books = []

##Functions
def add_book():
    book_id = input("\nEnter book ID: ")
    book_name = input("Enter book name: ")
    author = input("Enter author: ")
    is_available = True

    book = Book(book_id,book_name,author,is_available)
    books.append(book)

    with open("book.txt","w") as book_file:
        for book in books:
            book_file.write(f'\nBook ID - {book.book_id}\nBook name - {book.book_name}\nAuthor - {book.author}\n')
        print("\nBook added to the system and saved to the files successfully!\n")


def view_book():
    for book in books:
        print(f'\nBook ID - {book.book_id}\nBook name - {book.book_name}\nAuthor - {book.author}\nAvailable - {"Yes" if book.is_available else "No"}\n')


def delete_book():
    book_id = input("\nEnter book ID to remove: ")

    is_book_found = False

    for book in books:
        if book.book_id == book_id:
            books.remove(book)
            is_book_found = True
            print(f'\nBook with the book ID {book_id} has been removed from the system!\n')
            break
    
    if not is_book_found:
        print(f'\nBook with the book ID {book_id} not in the system\n')

    with open("book.txt","w") as book_file:
         for book in books:
             book_file.write(f'\nBook ID - {book.book_id}\nBook name - {book.book_name}\nAuthor - {book.author}\nAvailable - {"Yes" if book.is_available else "No"}\n')


def register_member():
    regi_number = input("\nEnter register number: ")
    name = input("Enter name: ")
    dob = input("Enter Date of birth(1998-03-12): ")

    member = Member(regi_number,name,dob)
    members.append(member)

    with open("member.txt","w") as member_file:
       for member in members:
            member_file.write(f'\nRegister number - {member.regi_number}\nMember name - {member.name}\nMember date of birth - {member.dob}\n')
       print("\nMember registered successfully and details saved to the files!\n")


def book_borrow_history(member,book):
    with open("book_borrow_history.txt","a") as history_file:
        
             history_file.write(f'\nRegister number - {member.regi_number}\nMember name - {member.name}\n')       
             history_file.write(f'Book ID - {book.book_id}\nBook name - {book.book_name}\nAuthor - {book.author}\n')
             print("\nBorrowing history updated successfully!\n")     
    

def view_borrow_history():
    register_number = input("\nEnter register number: ")
    history_found = False
    print(f'\nBorrowing history for register number {register_number}:')
    
    with open("book_borrow_history.txt","r") as history_file:
         for line in history_file:
             if register_number in line:
                 history_found = True
                 print(line.strip())

                 for _ in range(4):
                     print(next(history_file).strip())
                     print("--------------------------------------------")




         if not history_found :
                 print(f'\nNo borrowing history found for member register number: {register_number}\n')
        
        


def book_borrow():
    regi_number = input("\nEnter register number: ")
    is_member_found = False

    for member in members:
        if member.regi_number == regi_number:
             is_member_found = True
             book_id = input("Enter book ID: ")
             is_book_found = False

             for book in books:
                 if book.book_id == book_id:
                     is_book_found = True
                     if book.is_available:
                        book.is_available = False

                        print(f'\nBook ID {book_id} has been borrowed successfully by member register number {regi_number}.\n')                      
                        book_borrow_history(member,book)                             
                        break
                        
                        



                 if not is_book_found:
                     print(f'\nBook with book ID {book_id} not in the system\n')


             if is_member_found == False:
                 print(f'\nMember with register number {regi_number} not registered\n')


def book_return():
    
     regi_number = input("\nEnter register number: ")
     is_member_found = False

     for member in members:
         if member.regi_number == regi_number:
             is_member_found = True

             book_id=input("Enter book ID of book that return: ")
             is_book_found=False

             for book in books:
                 if book.book_id == book_id:
                     is_book_found=True
        
                     book.is_available = True

                     print(f'\nBook ID {book_id} has been returned successfully by member register number {regi_number}\n')                   
                     break
    
                 if not is_book_found:
                     print(f'\nok with bookBo ID {book_id} not in the system\n')


             if is_member_found == False:
                 print(f'\nMember with register number {regi_number} not registered\n')




##Main function

login = Login(username,password)

print("\nLIBRARY MANAGEMENT\n     SYSTEM\n")

while username != username1 or password != password1 :
    username = input("\nEnter username: ")
    password = input("Enter password: ")
       

    if username == username1 and password == password1 :
        print("\nLogin successfull!\n")
        
        choice=""

        while choice != "6":
            print("\n   MENU\n1.Register member\n2.Borrow / Return books\n3.Track borrowing history\n4.Add / Remove books\n5.View books\n6.Logout")
            choice = input("\nEnter choice number: ")

            if choice == "1":
                register_member()

            elif choice == "2":
                choice_1=""
                print("\n1.Borrow\n2.Return\n")
                choice_1= input("Enter choice number: ")
                if choice_1=="1":
                    book_borrow()

                elif choice_1=="2":
                    book_return()

                else:
                    print("\nInvalid choice try again!\n")
            
            
            elif choice == "3":
                view_borrow_history()


            elif choice == "4":
                admin_username=""
                admin_password=""

                admin_username1="admin"
                admin_password1="123"

                while admin_username != admin_username1 or admin_password != admin_password1:

                    print("\nACCESS ONLY FOR ADMINS!\n")

                    admin_username = input("\nEnter username: ")
                    admin_password = input("Enter password: ")

                    if admin_username == admin_username1 and admin_password == admin_password1:
                        print("\nAdmin loggin successful!\n")

                        choice_2=""

                        while choice_2 != "4":
                             print("\n1.Add book\n2.Remove book\n3.View books\n4.Menu")
                             choice_2 = input("Enter choice number: ")
                             if choice_2 == "1":
                                 add_book()
                             elif choice_2 == "2":
                                 delete_book()
                             elif choice_2 == "3":
                                 view_book()
                             elif choice_2 == "4":
                                 pass
                             else :
                                 print("\nInvalid choice! please try again\n")



                    elif admin_username == admin_username1 and admin_password != admin_password1:
                        print("\nInvalid password please try again!\n")

                    elif admin_username != admin_username1 and admin_password == admin_password1:
                        print("\nInvalid username please try again!\n")

                    else:
                        print("\nInvalid username and password please try again!\n")

            elif choice == "5":
                view_book()

            elif choice == "6":
                print("\nLoging out..\n")

            else:
                print("\nInvalid choice! please try again\n")









    else:
        print("\nIncorrect password try again!")



