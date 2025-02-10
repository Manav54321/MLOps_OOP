class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""\nWelcome to Chatbook! How would you like to proceed?
                           1. press 1 to sign up
                           2. press 2 to sign in
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit\n""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin() 
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("Goodbye")
            exit()

    def signup(self):
        email = input("Enter your email here --> ")
        pwd = input("Enter your password here --> ")
        self.username = email
        self.password = pwd
        print("You have successfully signed up!")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print("You need to sign up first!")
        else:
            uname = input("Enter your email here --> ")
            pwd = input("Enter your password here --> ")
            if uname == self.username and pwd == self.password:
                self.loggedin = True
                print("You have successfully signed in!")
            else:
                print("Incorrect email or password")
        print("\n")
        self.menu()


obj = chatbook()