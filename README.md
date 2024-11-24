# CaesarCipher
A Python script for generating strong, customizable passwords with a built-in random shift logic for enhanced security. The password includes a user-defined mix of lowercase letters, uppercase letters, and special characters.


Random Password Generator with Shift Logic
Overview

This Python program generates a secure and customizable password using a mix of lowercase letters, uppercase letters, and special symbols. It incorporates a random shift logic to make the passwords more secure by offsetting characters within their respective categories.
Features

    Customizable Password Composition:
        User inputs the desired number of lowercase letters, uppercase letters, and special characters.
    Random Shift Logic:
        A random shift value is applied to introduce additional randomness to the password.
    Shuffling:
        Final password characters are shuffled to ensure unpredictability.
    Simple and Lightweight:
        No external libraries required (uses only Python's built-in random module).

How It Works

    Input Parameters:
        Users specify how many lowercase letters, uppercase letters, and special characters the password should contain.
    Random Shift:
        Each character is selected based on a randomly determined shift to its position in the list of available characters.
    Password Construction:
        Characters are added to a list, shuffled, and then converted into a string to form the final password.

Usage

    Clone or download the script to your local environment.
    Run the script:

    python password_generator.py

    Follow the prompts to input your desired password configuration:
        Number of lowercase letters.
        Number of uppercase letters.
        Number of special characters.
    Copy and use the generated password!

Example Execution
User Input:

Vnesi kolku mali bukvi sakas da ima vo passwordot 5
Vnesi kolku golemi bukvi sakas da ima vo passwordot 3
Vnesi kolku znaci sakas da ima vo passwordot: 2

Output:

$aCeGtU!v
