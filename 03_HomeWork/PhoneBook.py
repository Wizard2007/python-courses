import sys
help ="""
- to add new contact type C;
- to display existsing contact type R;
- to update existing contact type U;
- to remove existsing contact type R;
- to print help type H;
- to terimate type Q
"""

print(help)

phoneBook = {}

while True:
    commandType = input("Enter command : ").upper
    if commandType == "C" :
        print("Add new contact.")
        name = input("Enter contact name : ")
        phone = input("Enter contact phone : ")
        phoneBook[name] = phone
        #print(phoneBook)
    elif commandType == "R":
        print("Display phone.")
        name = input("Enter contact name : ")
        try:
            print(phoneBook[name])
        except KeyError:
            print("Not found")
        except Exception as e:
            print(f"Error while delete contact. {e}")
        #print(phoneBook)
    elif commandType == "U":
        print("Update existing contact.")
        name = input("Enter contact name : ")
        phone = input("Enter contact phone : ")
        try:
            phoneBook[name] = phone
        except KeyError:
            if phone in phoneBook.items: 
                print("Name not found but phone already exists. Please delete coresponding contact.")
                print(phoneBook)
            else:
                print("Not found")
        except Exception as e:
            print(f"Error while delete contact. {e}")         
        #print(phoneBook)
    elif commandType == "D":
        print("Delete existing contact.")
        name = input("Enter contact name : ")
        try:
            phoneBook.pop(name)
        except KeyError:
            print("Not found.")
        except Exception as e:
            print(f"Error while delete contact. {e}")
        #print(phoneBook)
    elif commandType == "H":     
        print(help)
    elif commandType == "Q":
        print("Program terminated.")
        break
    else:
        print("Unknown command.")