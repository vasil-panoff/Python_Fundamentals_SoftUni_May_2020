email = input()

text_input = input()

while text_input != "Complete":
    args = text_input.split()
    command = args[0]

    if text_input == "Make Upper":
        email = email.upper()
        print(email)
    elif text_input == "Make Lower":
        email = email.lower()
        print(email)
    elif command == "GetDomain":
        count = int(args[1])
        domain = email[-count:]
        print(domain)
    elif command == "GetUsername":
        index = email.find("@")
        if index == -1:
            print(f"The email {email} doesn't contain the @ symbol.")
            text_input = input()
        else:
            print(email[:index])
    elif command == "Replace":
        char = args[1]
        email = email.replace(char, "-")
        print(email)
    elif command == "Encrypt":
        for ch in email:
            print(ord(ch), end=" ")

    text_input = input()
