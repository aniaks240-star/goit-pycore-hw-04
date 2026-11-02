def parse_input(user_input):
    parts = user_input.split()
    if not parts:
        return "", []
    return parts[0].casefold(), [part.casefold() for part in parts[1:]]


def add_contact(args, contacts):
    if len(args) != 2:
        return "Give me name and phone please."
    name, phone = args
    contacts[name.casefold()] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Give me name and phone please."
    name, phone = args
    name = name.casefold()
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Enter user name."
    return contacts.get(args[0].casefold(), "Contact not found.")


def show_all(args, contacts):
    if args:
        return "This command takes no arguments."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items()) or "No contacts."


def main():
    contacts = {}
    handlers = {"add": add_contact, "change": change_contact,
                "phone": show_phone, "all": show_all}
    print("Welcome to the assistant bot!")
    while True:
        try:
            command, args = parse_input(input("Enter a command: "))
        except (EOFError, KeyboardInterrupt):
            print("\nGood bye!")
            break
        if command in ("close", "exit") and not args:
            print("Good bye!")
            break
        if command == "hello" and not args:
            print("How can I help you?")
        elif command in handlers:
            print(handlers[command](args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
