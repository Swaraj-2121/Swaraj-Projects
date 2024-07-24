import datetime
user_info = {"Narendra": 1234,"Kunal": 2222,"Mohit": 4343}
student_info = {"Yuvraj": 2345,"Swami": 3434,"Gopal": 4545,"Komal": 6565}
Engineering = {"Java": 2, "C++": 50, "DSA": 90}
Agriculture = {"Livestock production": 50, "Crop production": 50, "agricultural economics": 50,
               "agricultural engineering": 50}
Pharmacy = {"Industrial Pharmacy": 50, "Pharmacology": 50, "Human Anatomy And Physiology": 60,
            "Pharmaceutical Engineering.": 70}

def user_check(username, password):
    if username in user_info.keys():
        if password == user_info[username]:
            print("You are log in.\n")
            while (True):
                print("1)Add Admin\n2)Add New Books To Library\n3)exit\n")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    add_admin()
                elif choice == 2:
                    add_new_books()
                elif choice == 3:
                    break
                else:
                    print("Enter Proper Choice.")
    else:
        print("Invalid Credentials.")
        re_user_check()


def re_user_check():
    re_user_name = input("Enter Username: ")
    re_pass_word = int(input("Enter Password: "))
    user_check(re_user_name, re_pass_word)


def add_admin():
    print(user_info)
    username = input("Enter Username: ")
    password = int(input("Enter Password: "))
    user_info[username] = password
    print(f"{username} has been added as admin.\n")


def add_new_books():
    branch = int(input("1)Engineering\n2)Pharmacy\n3)Agriculture"))
    book = input("Enter Name of Book: ")
    quantity = int(input("Enter Quantity of Book: "))
    if branch == 1:
        Engineering[book] = quantity
        print(f"{book} is added in Engineering Branch.\n")
    elif branch == 2:
        Pharmacy[book] = quantity
        print(f"{book} is added in Pharmacy Branch.\n")
    elif branch == 3:
        Agriculture[book] = quantity
        print(f"{book} is added in Agriculture Branch.\n")
    else:
        print("Enter Proper Choice.\n")


def student_check(username, password):
    if username in student_info.keys():
        if password == student_info[username]:
            print("You are log in.\n")
            while (True):
                print("1)Books Available\n2)Borrow Book\n3)Return Book\n4)Exit\n")
                choice = int(input("Enter Your Choice: "))
                if choice == 1:
                    books_available()
                elif choice == 2:
                    borrow_book()
                elif choice == 3:
                    return_book()
                elif choice == 4:
                    break
                else:
                    print("Enter Proper Choice.")
    else:
        print("Invalid Credentials.")
        re_student_check()


def re_student_check():
    re_user_name = input("Enter Username: ")
    re_pass_word = int(input("Enter Password: "))
    student_check(re_user_name, re_pass_word)


def books_available():
    branch = int(input("1)Engineering\n2)Pharmacy\n3)Agriculture\n"))
    if branch == 1:
        for k in Engineering:
            print(f"{k}={Engineering[k]}\n")
    elif branch == 2:
        for k in Pharmacy:
            print(f"{k}={Pharmacy[k]}\n")
    elif branch == 3:
        for k in Agriculture:
            print(f"{k}={Agriculture[k]}\n")
    else:
        print("Enter Proper Choice.\n")


def borrow_book():
    branch = int(input("1)Engineering\n2)Pharmacy\n3)Agriculture\n"))
    book = input("Enter Name Of Book: ")
    if branch == 1:
        if book in Engineering:
            if Engineering[book] > 0:
                print(f"You have issued the {book} Please keep book neat and clean and return within 30 days.\n")
                Engineering[book] = Engineering[book] - 1
                curent_date = datetime.datetime.now()
                with open("history.txt", "a") as f:
                    f.write(f"Username:{user_name}\nBranch:Engineering\nBook:{book}\nIssue Date and Time:{curent_date.day}/{curent_date.month}/{curent_date.year} {curent_date.time()}\n")
                    f.write("------------\n")
            else:
                print("Currently book is not available.\n")
        else:
            print("Book is not in library.\n")

    elif branch == 2:
        if book in Pharmacy:
            if Pharmacy[book] > 0:
                print(f"You have issued the {book} Please keep book neat and clean and return within 30 days.\n")
                Pharmacy[book] = Pharmacy[book] - 1
                curent_date = datetime.datetime.now()
                with open("history.txt", "a") as f:
                    f.write(f"Username:{user_name}\nBranch:Pharmacy\nBook:{book}\nIssue Date and Time:{curent_date.day}/{curent_date.month}/{curent_date.year} {curent_date.time()}\n")
                    f.write("------------\n")
            else:
                print("Currently book is not available.\n")
        else:
            print("Book is not in library.\n")
    elif branch == 3:
        if book in Agriculture:
            if Agriculture[book] > 0:
                print(f"You have issued the {book} Please keep book neat and clean and return within 30 days.\n")
                Agriculture[book] = Agriculture[book] - 1
                curent_date = datetime.datetime.now()
                with open("history.txt", "a") as f:
                    f.write(f"Username:{user_name}\nBranch:Agriculture\nBook:{book}\nIssue Date and Time:{curent_date.day}/{curent_date.month}/{curent_date.year} {curent_date.time()}\n")
                    f.write("------------\n")
            else:
                print("Currently book is not available.\n")
        else:
            print("Currently book is not available.\n")
    else:
        print("Enter Proper Choice.\n")


def return_book():
    branch = int(input("1)Engineering\n2)Pharmacy\n3)Agriculture\n"))
    book = input("Enter Name Of Book: ")
    if branch == 1:
        if book in Engineering:
            Engineering[book] = Engineering[book] + 1
            print(f"You have successfully returned {book}. Have A Great Day!\n")
            curent_date = datetime.datetime.now()
            with open("return_book.txt", "a") as f:
                f.write(f"Username:{user_name}\nBranch:Engineering\nBook:{book}\nReturn Date and Time:{curent_date.day}/{curent_date.month}/{curent_date.year} {curent_date.time()}\n")
                f.write("------------\n")
        else:
            print("You are returning book in wrong Branch.\n")
    elif branch == 2:
        if book in Pharmacy:
            Pharmacy[book] = Pharmacy[book] + 1
            print(f"You have successfully returned {book}. Have A Great Day!\n")
            curent_date = datetime.datetime.now()
            with open("return_book.txt", "a") as f:
                f.write(f"Username:{user_name}\nBranch:Pharmacy\nBook:{book}\nIssue Date and Time:{curent_date.day}/{curent_date.month}/{curent_date.year} {curent_date.time()}\n")
                f.write("------------\n")
        else:
            print("You are returning book in wrong Branch.\n")
    elif branch == 3:
        if book in Agriculture:
            Agriculture[book] = Agriculture[book] + 1
            print(f"You have successfully returned {book}. Have A Great Day!\n")
            curent_date = datetime.datetime.now()
            with open("return_book.txt", "a") as f:
                f.write(f"Username:{user_name}\nBranch:Agriculture\nBook:{book}\nIssue Date and Time:{curent_date.day}/{curent_date.month}/{curent_date.year} {curent_date.time()}\n")
                f.write("------------\n")
        else:
            print("You are returning book in wrong Branch.\n")
    else:
        print("Enter Proper Choice.\n")


# driver code
if __name__ == "__main__":
    print("--------------Welcome To Library--------------")
    while (True):
        user_type = ''' 
        1)Admin
        2)Student
        3)Exit
        '''
        print(user_type)
        user = int(input("Enter Type Of User: "))
        if user == 1:
            user_name = input("Enter Username: ")
            pass_word = int(input("Enter Password: "))
            user_check(user_name, pass_word)
        elif user == 2:
            log_sign=int(input("1)Log in\n2)Sign up"))
            if log_sign==1:
                user_name = input("Enter Username: ")
                pass_word = int(input("Enter Password: "))
                student_check(user_name, pass_word)
            elif log_sign==2:
                new_user = input("Enter Username: ")
                new_pass = int(input("Enter Password: "))
                student_info[new_user]=new_pass
                print(f"Your account has been created. Have a great day!")
            else:
                break


        elif user == 3:
            exit()
        else:
            print("Enter Proper Choice.")
