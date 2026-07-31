# Caesar Cipher 🔐

A simple Python implementation of the classic Caesar Cipher encryption and decryption algorithm.  
This project allows users to encode and decode secret messages by shifting letters of the alphabet.

---

## 📖 Features
- Encrypt (`encode`) and decrypt (`decode`) messages.
- Handles spaces, numbers, and symbols gracefully (they remain unchanged).
- Supports restarting the program for multiple runs.
- ASCII art logo displayed at startup (imported from `art.py`).
- Shift values wrap around the alphabet (e.g., shifting `z` by 1 becomes `a`).

---

## 🛠️ How It Works
1. The user chooses whether to **encode** or **decode**.
2. They enter a message.
3. They provide a shift number.
4. The program outputs the transformed message.
5. The user can choose to run the cipher again or exit.

---

## ▶️ Example Usage
```text
Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world!
Type the shift number:
3
Here is the encoded result: khoor zruog!
Type 'yes' if you want to go again. Otherwise, type 'no':
no
Goodbye!

