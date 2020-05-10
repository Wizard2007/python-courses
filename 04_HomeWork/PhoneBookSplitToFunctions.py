def terminate_execution():
    global continueExecution
    continueExecution = False
    print("Program terminated.")


def prompt_value(prompt):
    value = ""
    while not value:
        value = input(prompt)
    return value


def add_contact_to_phone_book(name, phone):
        try:
            phone_book[name] = phone
        except Exception as e:
            print(e)


def add_contact():
        print("Add new contact.")

        name = prompt_value(ENTER_NAME)
        phone = prompt_value(ENTER_PHONE)
        add_contact_to_phone_book(name, phone)


def display_help():
    print(HELP)


def print_contact_by_name(name):
    try:
        print(phone_book[name])
    except KeyError:
        print(NOT_FOUND)
    except Exception as e:
        print(e)


def display_contact():
    print("Display phone.")

    name = prompt_value(ENTER_NAME)
    print_contact_by_name(name)


def update_contact_in_phone_book(name, phone):
    try:
        phone_book[name] = phone
    except KeyError:
        if phone in phone_book.items: 
            print("Name not found but phone already exists. Please delete coresponding contact.")
        else:
            print(NOT_FOUND)
    except Exception as e:
        print(e)


def update_contact():
    print("Update existing contact.")
    
    name = prompt_value(ENTER_NAME)
    phone = prompt_value(ENTER_PHONE)
    update_contact_in_phone_book(name, phone)


def delete_contact_by_name(name):
    try:
        del phone_book[name]
    except KeyError:
        print(NOT_FOUND)
    except Exception as e:
        print(e)


def delete_contact():
    print("Delete existing contact.")

    name = prompt_value(ENTER_NAME)
    delete_contact_by_name(name)   


HELP ="""
- to add new contact type C;
- to display existsing contact type R;
- to update existing contact type U;
- to remove existsing contact type D;
- to print help type H;
- to terimate type Q.
"""

ENTER_NAME = "Enter contact name : "
ENTER_PHONE = "Enter contact phone : "
NOT_FOUND = "Not found."

display_help()

phone_book = {}
continueExecution = True

while continueExecution:
    name = ""
    phone = ""
    command_type = input("Enter command : ").upper()
    if command_type == "C" :
        add_contact()
    elif command_type == "R":
        display_contact()
    elif command_type == "U":
        update_contact()
    elif command_type == "D":
        delete_contact()
    elif command_type == "H":     
        display_help()
    elif command_type == "Q":
        terminate_execution()
    else:
        print("Unknown command.")


