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
            self.my_post()
        elif user_input == "4":
            self.send_msg()
        else:
            print("Have a great day!")
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

    def my_post(self):
        if self.loggedin == True:
            txt = input("Write your post here --> ")
            print(f"Your post {txt} has been published!")
        else:
            print("You need to sign in first to write a post!")
        print("\n")
        self.menu()

    def send_msg(self):
        if self.loggedin == True:
            friend = input("Enter your friend's name here --> ")
            msg = input("Enter your message here --> ")
            print(f"Your message has been sent to {friend}")
        else:
            print("You need to sign in first to send a message!")
        print("\n")
        self.menu()


obj = chatbook()