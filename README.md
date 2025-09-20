# CrypText

**CrypText** is a lightweight command-line cryptographic utility written in Python for text encryption and decryption using a custom Caesar cipher logic. Built for cybersecurity learners, CTFers, and crypto enthusiasts, it’s designed to work seamlessly on both **Termux** and traditional Linux terminals.

---

## Features

- Encrypt and decrypt messages using a Caesar cipher
- Custom key input for better flexibility
- Works on **Android (via Termux)** and **Linux desktops**
- Beginner-friendly, minimal setup
- Easy to expand for stronger crypto methods

---

## Use Case

This tool is perfect for:
- Quick text encryption/decryption on the go
- CTF players working with Caesar or basic substitution ciphers
- Educators teaching cryptographic fundamentals
- Cybersecurity learners building Python projects

---

## STEPS FOR USING IT IN TERMUX OR KALI

cd cryptext

pkg install python (FOR TERMUX)
python3 cryptext.py

Do you want to encrypt or decrypt? encrypt
Enter your message: CyberSecIsCool
Enter the encryption key (1-25): 5

Encrypted Message: DzgjwXjhNxHttq


Do you want to encrypt or decrypt? decrypt
Enter your message: DzgjwXjhNxHttq
Enter the encryption key (1-25): 5

Decrypted Message: CyberSecIsCool

File Structure
Termu-Crypt/
├── cryptext.py
├── README.md 
├── requirements.txt
---------------------------------------


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Magnus7811/cryptext.git
