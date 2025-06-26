# Функція обробки рядку, який ввів користувач

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

# Функція для додавання нового контакту

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# Функція для зміни номеру існуючого контакту

def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact for {name} has been updated"
    else:
        return "Contact doesn't exist"

# Функція для виводу номеру телефону контакта

def phone(args, contacts):
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found"
    
# Функція для виводу усіх контактів

def show_all_contacts(contacts):
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

# Основна функція, яка зчитує команди від юзера і виконує відповідні дії

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close","exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "number":
            print(phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()