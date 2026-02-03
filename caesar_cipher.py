def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - start + shift) % 26 + start)
            else:
                result += chr((ord(char) - start - shift) % 26 + start)
        else:
            result += char

    return result


message = input("Enter the message: ")
shift = int(input("Enter shift value: "))
choice = input("encrypt / decrypt: ").lower()

print("Result:", caesar_cipher(message, shift, choice))