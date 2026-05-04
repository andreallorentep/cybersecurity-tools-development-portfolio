# Password Generator

## Overview
This project is a Python-based **educational password generation and management tool** designed to promote **strong password practices and secure credential storage**.

The tool generates **random, high-entropy passwords** using combinations of uppercase letters, lowercase letters, numbers, and special characters. It also allows users to **store and view generated passwords locally** in a structured JSON file.

This project demonstrates how password generators work and highlights the importance of **strong password creation in cybersecurity practices**, helping reduce the risk of **brute-force attacks, credential stuffing, and password guessing**.

## Features
- Secure random password generation
- Customizable password length
- Combination of letters, numbers, and special characters
- Option to save generated passwords
- Local password storage using JSON
- View previously saved passwords
- Interactive command-line interface
- Simple credential management system

## Technologies Used
- Python
- random library
- string module
- json module
- os module
- File handling operations
- Command-line interface (CLI)

## How It Works
The password generator creates strong passwords by randomly selecting characters from multiple character sets.

1. The user launches the program.
2. The user selects the option to generate a new password.
3. The user specifies the desired password length.
4. The program generates a random password using letters, digits, and symbols.
5. The user can choose whether to save the password.
6. If saved, the password is stored in a **JSON file associated with a service name**.
7. The user can view all stored passwords from the menu.

This process demonstrates how password generators can help users maintain **strong and unique passwords across different services**.

## Example Output

Password Generator  
Cybersecurity Utility Tool  


Choose an option:
1 Generate new password  
2 View saved passwords  
3 Exit  

Select option: 1

Enter password length: 12

Generated Password:
)@\"bdw{:{*N>

Do you want to save this password? y  
Enter service name: test 

Password saved for: test

Choose an option:

1 Generate new password  
2 View saved passwords  
3 Exit  

Select option: 2

Saved Passwords

test : )@\"bdw{:{*N>

## Output File
The program stores passwords in a local JSON file:

passwords.json

Example structure:
{

    "test": ")@\"bdw{:{*N>"
    
}

Each entry contains:

Service name → the account or platform
Generated password → the stored credential

## Installation

Clone the repository or download the project.

Run the tool using Python:

python password_generator.py

No external dependencies are required because the program uses only Python's standard libraries.

## Disclaimer

This tool is intended for educational purposes to demonstrate password generation techniques and basic credential management.

Passwords stored in the JSON file are not encrypted, so this tool should not be used to store real sensitive credentials in production environments.
For real-world applications, password managers should implement strong encryption and secure storage mechanisms.