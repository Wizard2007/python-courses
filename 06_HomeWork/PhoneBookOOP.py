NOT_FOUND = "Not found."

def handle_exception_decorator_factory(input_func):
    def wrapper_exception(*args, **kwargs):
        try:
            return input_func(*args, **kwargs)
        except Exception as e:
            print(e)
    return wrapper_exception


def handle_key_error_decorator_factory(input_func):
    def wrapper_key_error(*args, **kwargs):
        try:
            return input_func(*args, **kwargs)
        except KeyError as e:
            print(NOT_FOUND)
    return wrapper_key_error


class PhoneBookRepository:
    def __init__(self):
        self.phone_book = {}
        self.NOT_FOUND = NOT_FOUND
    @handle_exception_decorator_factory
    def add_contact_to_phone_book(self, name, phone):
        self.phone_book[name] = phone
    @handle_exception_decorator_factory
    def update_contact_in_phone_book(self, name, phone):
        try:
            self.phone_book[name] = phone
        except KeyError:
            if phone in phone_book.items: 
                print("Name not found but phone already exists. Please delete coresponding contact.")
            else:
                print(NOT_FOUND)
    @handle_key_error_decorator_factory
    @handle_exception_decorator_factory
    def delete_contact_by_name(self, name):
        del self.phone_book[name]
    @handle_key_error_decorator_factory
    @handle_exception_decorator_factory
    def get_phopne_by_name(self, name):
        return self.phone_book[name]


class PhoneBookServiceCli:
    def __init__(self, phoneBookRepository):
        self.phoneBookRepository = phoneBookRepository
        self.promptValueFunc = None
        self.ENTER_NAME = "Enter contact name : "
        self.ENTER_PHONE = "Enter contact phone : "


    def _prompt_value(self, promptString):
        print(self.promptValueFunc)
        if self.promptValueFunc:
            return self.promptValueFunc(promptString)
        else:
            raise NameError()

    def add_contact(self):
        print("Add new contact.")

        name = self._prompt_value(ENTER_NAME)
        phone = self._prompt_value(ENTER_PHONE)
        self.phoneBookRepository.add_contact_to_phone_book(name, phone)
    def display_contact(self):
        print("Display phone.")

        name = self._prompt_value(ENTER_NAME)
        print(self.phoneBookRepository.get_phopne_by_name(name))
    def update_contact(self):
        print("Update existing contact.")
        
        name = self._prompt_value(ENTER_NAME)
        phone = self._prompt_value(ENTER_PHONE)
        self.phoneBookRepository.update_contact_in_phone_book(name, phone)
    def delete_contact(self):
        print("Delete existing contact.")

        name = self._prompt_value(ENTER_NAME)
        self.phoneBookRepository.delete_contact_by_name(name)

class CliExecutor:
    def __init__(self, phoneBookServiceCli):
        self.continueExecution = True
        self.phoneBookServiceCli = phoneBookServiceCli
        self.phoneBookServiceCli.promptValueFunc = self.prompt_value;
        self.HELP ="""
            - to add new contact type C;
            - to display existsing contact type R;
            - to update existing contact type U;
            - to remove existsing contact type D;
            - to print help type H;
            - to terimate type Q.
            """

    def start_terminal_session(self):
        self.display_help()

        while self.continueExecution:
            command_type = input("Enter command : ").upper()
            if command_type == "C" :
                self.phoneBookServiceCli.add_contact()
            elif command_type == "R":
                self.phoneBookServiceCli.display_contact()
            elif command_type == "U":
                self.phoneBookServiceCli.update_contact()
            elif command_type == "D":
                self.phoneBookServiceCli.delete_contact()
            elif command_type == "H":     
                self.phoneBookServiceCli.display_help()
            elif command_type == "Q":
                self.terminate_execution()
            else:
                print("Unknown command.")


    def terminate_execution(self):
        self.continueExecution = False
        print("Program terminated.")


    def prompt_value(self, prompt):
        value = ""
        while not value:
            value = input(prompt)
        return value

    def display_help(self):
        print(self.HELP)


cliExecutor = CliExecutor(PhoneBookServiceCli(PhoneBookRepository()))

cliExecutor.start_terminal_session()

