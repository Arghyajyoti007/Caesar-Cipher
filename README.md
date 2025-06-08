# 🔐 Caesar Cipher CLI Tool (Python)

A beginner-friendly Python implementation of the classic **Caesar Cipher** encryption and decryption technique. This command-line tool lets users **encode** and **decode** secret messages using a shift key.

---

## 📌 What is Caesar Cipher?

The **Caesar Cipher** is a simple and ancient encryption technique where each letter in a message is shifted a certain number of positions in the alphabet.

For example, with a shift of 3:  
HELLO → KHOOR  

---

## 🧠 Features

- Encrypt and decrypt text using Caesar Cipher logic.
- Handles spaces, punctuation, and special characters (keeps them unchanged).
- Works with both uppercase and lowercase inputs.
- Option to repeat encryption/decryption operations.
- ASCII logo display from external module.

---

## 🛠️ Technologies Used

- Python 3.x
- Custom modules:
  - `Day8_CaesarCipherAlphabet` – for the alphabet list.
  - `Day8_CaesarCipherArt` – for the ASCII logo.

---

## 📁 Project Structure  
Day8_CaesarCipher/  
│
├── main.py # This file (contains all logic)  
├── Day8_CaesarCipherAlphabet.py # Contains: alphabet = ['a', ..., 'z']  
└── Day8_CaesarCipherArt.py # Contains: logo = "ASCII Art Here"  


## 📷 Sample Output    

```
    _____                    _                   
  / ____|                  | |                  
 | |     __ _ ___  ___  ___| |_ ___  _ __ ___   
 | |    / _` / __|/ _ \/ __| __/ _ \| '__/ _ \
 | |___| (_| \__ \  __/\__ \ || (_) | | |  __/
  \_____\__,_|___/\___||___/\__\___/|_|  \___|  

Enter 'E' for Encrypt; Enter 'D' for Decrypt : E  
Enter your message : HELLO  
Enter the shift amount: 3  
Here is the Encrypted message : khoor  
Do you want to go again? 'Y' for 'Yes' & 'N' for 'NO' : Y
```
... 

...


