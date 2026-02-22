from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return "Enter the argument for the command"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

class ContactsManager:
    contacts = {}

    @input_error
    def add(self, args):
        name, phone = args
        self.contacts[name] = phone
        return "Contact added."

    @input_error
    def change(self, args):
        name, phone = args
        self.contacts[name] = phone
        return "Contact updated."

    @input_error
    def phone(self, args):
        [name] = args
        phone = self.contacts.get(name)
        return f"Phone number of {name} is {phone}." if phone else f"Contact {name} not found."

    def all(self):
        if len(self.contacts) == 0:
            return "No contacts in the list."
        return "\n".join(f"{name}: {phone}" for name, phone in self.contacts.items())

    def invalid(self):
        return "Invalid command."


def main():
    contacts = ContactsManager()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit"]:
            print("Good bye!")
            break
        elif hasattr(contacts, command):
            print(getattr(contacts, command)(args))
        else:
            print(contacts.invalid())

if __name__ == "__main__":
    main()