## Real-Time Password Checker: Intelligent Password Validation System
## About

The Real-Time Password Checker is a Python-based system designed to enhance user account security by providing instant feedback on password strength. Weak passwords are a major cause of security breaches, and this project addresses that issue by enforcing industry-standard rules for strong passwords.

The system checks passwords for minimum length, inclusion of uppercase and lowercase letters, digits, and special characters. It runs in a continuous loop, allowing users to enter multiple passwords without restarting the program. By providing clear, real-time guidance, it educates users and encourages best security practices.

This project is lightweight, portable, and suitable for educational purposes, personal security tools, or integration into small-scale applications.

## Features

## Real-Time Password Strength Evaluation
Instantly checks for minimum 8-character length, uppercase/lowercase letters, digits, and special characters.

## Continuous Input Loop
Allows users to check multiple passwords without restarting the program.

## User-Friendly Console Messages
Provides clear feedback on missing password requirements.

## Exit Command Support
Users can type exit at any time to safely terminate the program.

## Lightweight and Portable
Runs on standard Python environments without heavy dependencies.

## Requirements
Operating System:

Windows 10 / Ubuntu 18+ (64-bit)

## Programming Environment:

Python 3.8 or later

Libraries / Modules:

re (Regular Expressions)

Standard Python library

IDE / Platform:

VS Code / PyCharm / Thonny / Online Python Compiler (Programiz, Replit)

## System Architecture:
<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/acf88491-7a30-4b38-8e8b-fc50217815ba" />

## Source Code
```
import re

def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one number."
    if not re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/]", password):
        return "Password must contain at least one special character."
    return "Password is strong!"

# Loop for continuous password checking
while True:
    password = input("\nEnter your password (or type 'exit' to stop): ")
    if password.lower() == "exit":
        print("Program stopped.")
        break
    print(check_password(password))
```

## Output
## Weak Password (Length Issue)
Enter your password (or type 'exit' to stop): hello
Password must be at least 8 characters long.
<img width="1555" height="768" alt="image" src="https://github.com/user-attachments/assets/c6d79078-ba3c-4f3d-a835-b6f32e3fee7d" />


## Weak Password (Missing Special Character)
Enter your password (or type 'exit' to stop): Hello123
Password must contain at least one special character.
<img width="1440" height="771" alt="image" src="https://github.com/user-attachments/assets/e865aedc-464b-4aad-a111-96140736f303" />


## Strong Password + Exit
Enter your password (or type 'exit' to stop): Hello@123
Password is strong!
<img width="1440" height="771" alt="image" src="https://github.com/user-attachments/assets/2ac3f040-ff77-4202-a1a2-ad4cfe88e3a6" />

Enter your password (or type 'exit' to stop): exit
Program stopped.
<img width="1598" height="765" alt="image" src="https://github.com/user-attachments/assets/8f710db9-fd44-4ced-a99b-e8c42d2a00ae" />

## Results 
The Real-Time Password Checker improves user security by providing instant feedback on password strength, reducing the risk of weak passwords being used.
