import base64
from termcolor import cprint

def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            encrypted += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            encrypted += char
    return encrypted

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    return base64.b64decode(text.encode()).decode()

def main():
    cprint("=== CrypText ===", "cyan")
    cprint("[1] Caesar Encrypt\n[2] Caesar Decrypt\n[3] Base64 Encode\n[4] Base64 Decode", "yellow")
    
    choice = input("Choose option: ").strip()
    text = input("Enter text: ")

    if choice == "1":
        shift = int(input("Enter shift: "))
        cprint("Encrypted: " + caesar_encrypt(text, shift), "green")
    elif choice == "2":
        shift = int(input("Enter shift: "))
        cprint("Decrypted: " + caesar_decrypt(text, shift), "green")
    elif choice == "3":
        cprint("Encoded: " + base64_encode(text), "green")
    elif choice == "4":
        try:
            cprint("Decoded: " + base64_decode(text), "green")
        except:
            cprint("Invalid Base64 input!", "red")
    else:
        cprint("Invalid option!", "red")

if __name__ == "__main__":
    main()
