"""This displays the menu"""

print("---------- WELCOME TO THE TICKET HUB --------------")
print("---------------------------------------------------")

name = input("Enter Name to check ticket status: ")

"""This iterates to check for name given"""

def register_checker(name):
    f = open('ordinary_list.txt', 'r') 
    ordinary = f.read().split('\n')
    
    f = open('vip_list.txt', 'r') 
    vip = f.read().split('\n')

    for n in ordinary:
        input = n.split()
        if name == n or name == input[0] or name == input[1]:
            return str(n) + ' is ordinary' 
          
    for n in vip:
        input = n.split()
        if name == n or name == input[0] or name == input[1]:
            return str(n) +  ' is vip' 

    return name + ' is not on any list'       

"""This returns method"""
while True: 
    print(register_checker(name))
    close = input("Enter Another Name: ")
    if close == 'No':
        break




             