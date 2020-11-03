message = input()

data = input()
while "Reveal" != data:
    tokens = data.split(":|:")
    command = tokens[0]
    if "InsertSpace" == command:
        index = int(tokens[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif "Reverse" == command:
        substring = tokens[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            message += substring[::-1]
            print(message)
        else:
            print("error")
    elif "ChangeAll" == command:
        substring = tokens[1]
        replacement = tokens[2]
        message = message.replace(substring, replacement)
        print(message)
    data = input()
print(f"You have a new text message: {message}")