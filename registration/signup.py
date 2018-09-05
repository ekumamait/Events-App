vip_list = []
ordinary_list = []

class Registration():

    def __init__(self):
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
            vip_list.append(self.details)
        elif category == "ordinary":
            ordinary_list.append(self.details)
        else:
            return "Choose a Category"
        
    # def submit(self, username, email, category):
    #     """ This method submits all user details to category list """
    #     if self.details == "vip":
    #         vip_list.append(self.details)
    #         print("Vip Ticket Booked")
    #     elif self.details == "ordinary":
    #         ordinary_list.append(self.details)
    #         print("Ordinary Ticket Booked")
    #     else:    
    #         print("Oops, Booking Error")    
 


        