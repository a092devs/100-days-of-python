from art import logo


def caesar(message, shift):
    result = ""
    for letter in range(len(message)):
        char = message[letter]
        if ord(char) >= 65 and ord(char) <= 91:
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif ord(char) >= 97 and ord(char) <= 122:
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += str(message[letter])
    return result


print(logo)

while True:
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n(Enter a negative number to decode)\n"))
    print(f"Plain text: {text}")
    print(f"Shift number: {shift}")
    print(f"Cipher: {caesar(text, shift)}")
    start_again = input(
        "\nDo you want to encode\decode another message?\nType 'y' for yes and 'n' for no.\n"
    ).lower()
    if start_again in ["no", "n"]:
        break
