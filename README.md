# CaesarCipher
A simple implementation of the Caesar Cipher for encryption and decryption. The program allows users to input a text, specify a shift parameter, and choose to either encrypt or decrypt the text. It preserves the case of letters and handles non-alphabetic characters gracefully.


Caesar Cipher: Encrypt and Decrypt Text
Overview

This project is a Python-based implementation of the Caesar Cipher, a classic encryption technique. It enables users to encrypt and decrypt text using a shift parameter. The program ensures that uppercase letters remain uppercase and handles non-alphabetic characters without modification.
Features

    Encrypt or Decrypt: Choose between encrypting or decrypting text.
    Customizable Shift: Specify a shift parameter to control how letters are transformed.
    Case Preservation: Maintains uppercase and lowercase letters in their respective cases.
    Handles Non-Alphabetic Characters: Non-alphabetic characters remain unchanged.

How It Works

    Encryption: Each letter in the input text is shifted forward by the given number of positions in the alphabet.
    Decryption: Each letter is shifted backward by the given number of positions in the alphabet.
    Wrap-Around: The program uses modular arithmetic to ensure that shifts wrap around the end of the alphabet (e.g., shifting "z" forward results in "a").

Usage

    Clone the repository or download the script.
    Run the script using Python:

    python caesar_cipher.py

    Follow the input prompts:
        Enter s for encryption or d for decryption.
        Provide the text to process.
        Specify the shift parameter as an integer.

Example Execution
Encryption

Enter 's' for encryption or 'd' for decryption: s
Enter text: Hello World
Enter shift parameter (integer): 3
Encrypted text: khoor zruog

Decryption

Enter 's' for encryption or 'd' for decryption: d
Enter text: khoor zruog
Enter shift parameter (integer): 3
Decrypted text: hello world
