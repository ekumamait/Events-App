class Registration():

    def __init__(self):
        self.vip_list = []
        self.ordinary_list = []
        self.details = {}
        
    def username(self, username):
        """ This method adds a username to the guests details """
        if username == "":
            return "Enter a Username"
        else:
            self.details["username"] = username

    def email(self, email):
        """ This method adds an email to the guests details """
        if email == "":
            return "Enter an Email"
        else:
            self.details["email"] = email

    def category(self, category):
        """ This method adds a category to the guests details """
        if category == "vip":
            self.vip_list.append(self.details)
        elif category == "ordinary":
            self.ordinary_list.append(self.details)
        else:
            return "Choose a Category"
        
    def submit(self, username, email, category):
        """ This method submits all user details to category list """
        if self.details == "vip":
            self.vip_list.append(self.details)
            print("Vip Ticket Booked")
        elif self.details == "ordinary":
            self.ordinary_list.append(self.details)
            print("Ordinary Ticket Booked")
        else:    
            print("Oops, Booking Error")    
 


        