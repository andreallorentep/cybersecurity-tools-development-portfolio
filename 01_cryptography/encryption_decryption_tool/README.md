# Encryption / Decryption Tool

## Overview
This project is a simple Python-based tool that allows users to encrypt and decrypt messages using symmetric cryptography. It demonstrates the basic implementation of secure message handling using the Fernet module from the cryptography library.

Fernet uses an AES-based encryption scheme to ensure confidentiality and integrity of the data.

## Features
- Encrypt plaintext messages
- Decrypt previously encrypted messages
- Command-line interface
- Uses secure symmetric encryption

## Technologies Used
- Python
- cryptography library
- Fernet (AES-based encryption)

## How It Works
The program generates a cryptographic key and uses it to encrypt and decrypt messages entered by the user through the terminal.

1. The user selects an option from the menu.
2. A message is provided for encryption or decryption.
3. The program processes the input and returns the result.

## Installation

Install the required dependency:
pip install cryptography

## Disclaimer
This tool is intended for educational purposes and for use on networks you own or have permission to test.