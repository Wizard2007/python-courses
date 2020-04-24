HELP ="""
- to add new contact type C;
- to display existsing contact type R;
- to update existing contact type U;
- to remove existsing contact type R;
- to print help type H;
- to terimate type Q.
"""

ENTER_NAME = "Enter contact name : "
ENTER_PHONE = "Enter contact phone : "
NOT_FOUND = "Not found."

print(HELP)

phone_book = {}

while True:
    name = ""
    phone = ""
    command_type = input("Enter command : ").upper()
    if command_type == "C" :
        print("Add new contact.")

        while not name:
            name = input(ENTER_NAME)

        while not phone:
            phone = input(ENTER_PHONE)

        try:
            phone_book[name] = phone
        except Exception as e:
            print(e)
    elif command_type == "R":
        print("Display phone.")

        while not name:
            name = input(ENTER_NAME)

        try:
            print(phone_book[name])
        except KeyError:
            print(NOT_FOUND)
        except Exception as e:
            print(e)
    elif command_type == "U":
        print("Update existing contact.")
        
        while not name:
            name = input(ENTER_NAME)
        
        while not phone:
            phone = input(ENTER_PHONE)

        try:
            phone_book[name] = phone
        except KeyError:
            if phone in phone_book.items: 
                print("Name not found but phone already exists. Please delete coresponding contact.")
            else:
                print(NOT_FOUND)
        except Exception as e:
            print(e)      
    elif command_type == "D":
        print("Delete existing contact.")

        while not name:
            name = input(ENTER_NAME)
        
        try:
            del phone_book[name]
        except KeyError:
            print(NOT_FOUND)
        except Exception as e:
            print(e)
    elif command_type == "H":     
        print(HELP)
    elif command_type == "Q":
        print("Program terminated.")
        break
    else:
        print("Unknown command.")