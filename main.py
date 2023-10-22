def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Incorrect number of arguments. Usage: add <name> <phone>"
    
def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return f"Phone number for {name} changed."
        else:
            return "Contact not found."
    except ValueError:
        return "Incorrect number of arguments. Usage: change <name> <phone>"

def get_phone(args, contacts):
    try:
        name, = args
        return contacts.get(name, "Contact not found.")
    except ValueError:
        return "Incorrect number of arguments. Usage: phone <name>"

def list_all_contacts(_, contacts):
    return '\n'.join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye! I'm stepping through the door!")
            break
        elif command == "hello":
            print("How can I help you? Do you hear me, Major Tom?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(list_all_contacts(args, contacts))
        else:
            print("Invalid command. Can you hear me, Major Tom?")

if __name__ == "__main__":
    main()