# Encryption / Descryption Tool
# Cybersecurity Portfolio Project

from cryptography.fernet import Fernet

#🔑 Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

#🔐 Encrypt function
def encrypt_message(message):
    encrypted = cipher.encrypt(message.encode())
    return encrypted

#🔓 Decrypt function
def decrypt_message(encrypted_message):
    decrypted = cipher.decrypt(encrypted_message.encode()).decode()
    return decrypted

#🧠 Main program
def main():
    while True:
        print("===================================")
        print(" Encryption / Decryption Tool")
        print("===================================")

        print("\nSelect an option:")
        print("1. Encrypt message")
        print("2. Decrypt message")
        print("3. Exit")

        choice = input("\nEnter choice (1/2/3): ")

        if choice == "1":
            print("\n[Encryption selected]")
            message = input("Enter message to encrypt: ")
            encrypted = encrypt_message(message)
            print("\nEncrypted message:")
            print(encrypted)

        elif choice == "2":
            print("\n[Decryption selected]")
            encrypted_message = input("Enter message to decrypt: ")
            decrypted = decrypt_message(encrypted_message)
            print("\nDecrypted message:")
            print(decrypted)
    
        elif choice == "3":
            print("Exiting program...")
            break

        else:
            print("\nInvalid option, try again")


#🚀 Entry point
if __name__ == "__main__":
    main()