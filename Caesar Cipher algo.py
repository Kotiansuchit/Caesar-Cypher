def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  # non-alphabetic characters are not changed
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()

    if choice not in ['encrypt', 'decrypt']:
        print("Invalid choice.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return

    if choice == 'encrypt':
        encrypted = encrypt(message, shift)
        print("Encrypted message:", encrypted)
    else:
        decrypted = decrypt(message, shift)
        print("Decrypted message:", decrypted)

if __name__ == "__main__":
    main()
