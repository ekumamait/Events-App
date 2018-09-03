"""This displays the menu"""

print("---------- WELCOME TO THE TICKET HUB --------------")
print("---------------------------------------------------")

name = input("Enter Name to check ticket status: ")

"""This iterates to check for name given"""

def register_checker(name):
    vip_list = []
    ordinary_list = []
    all_guests = []

    f = open('ordinary_list.txt', 'r') 
    ordinary = f.read().split('\n')
    ordinary_list = ordinary

    f = open('vip_list.txt', 'r') 
    vip = f.read().split('\n')
    vip_list = vip

    all_guests.append(ordinary_list)
    all_guests.append(vip_list)

    f.close()

    for n in all_guests[0]:
        input = n.split()
        if name == n or name == input[0] or name == input[1]:
            return str(n) + ' is ordinary' 
          
    for n in all_guests[1]:
        input = n.split()
        if name == n or name == input[0] or name == input[1]:
            return str(n) +  ' is vip' 

    return name + ' is not on any list' 
    
"""This returns method"""
print(register_checker(name))


        