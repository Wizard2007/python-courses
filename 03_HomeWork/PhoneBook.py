import sys
help = "- to add new user type C;\n- to display existsing user type R;\n- to update existing user type U;\n- to remove existsing user type R;\n- to print help type H;\n- to terimate type Q"

print(help)

phoneBook = {}

while True:
    commandType = input("Enter command : ")
    if commandType == "C" :
        print("Add new user.")
        name = input("Enter contact name : ")
        phone = input("Enter contact phone : ")
        phoneBook[name] = phone
        print(phoneBook)
    elif commandType == "R":
        print("Display phone.")
        name = input("Enter contact name : ")
        try:
            print(phoneBook[name])
        except KeyError:
            print("Not found")
        except:
            print("Error while delete user." + sys.exc_info()[0])
        print(phoneBook)
    elif commandType == "U":
        print("Update existing user.")
        name = input("Enter contact name : ")
        phone = input("Enter contact phone : ")
        try:
            phoneBook[name] = phone
        except KeyError:
            if phone in phoneBook.items: 
                print("Name not found but phone already exists. Please delete coresponding user.")
                print(phoneBook)
            else:
                print("Not found")
        except:
            print("Error while delete user." + sys.exc_info()[0])            
        print(phoneBook)
    elif commandType == "D":
        print("Delete existing user.")
        name = input("Enter contact name : ")
        try:
            phoneBook.pop(name)
        except KeyError:
            print("Not found")
        except:
            print("Error while delete user." + sys.exc_info()[0])
        print(phoneBook)
    elif commandType == "H":     
        print(help)
    elif commandType == "Q":
        print("Program terminated")
        break
    else:
        print("Unknown command")