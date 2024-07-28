def decode_message(message):
    keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
    decoded_message = ""
    for char in message:
        if char == " ":
            decoded_message += " "
        else:
            index = keyboard.index(char)
            decoded_message += keyboard[index - 1]
    return decoded_message

def main():
    while True:
        try:
            message = input()
            print(decode_message(message))
        except EOFError:
            break

if __name__ == "__main__":
    main()
