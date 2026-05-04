# 🔐 Password Generator & Local Password Saver
# Cybersecurity Utilities Project

import random
import string
import json
import os

print("===================================")
print(" Password Generator")
print(" Cybersecurity Utility Tool")
print("===================================\n")

# 📁 Configuration

# Folder where the script is located
SCRIPT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Full path to passwords.json
PASSWORD_FILE = os.path.join(SCRIPT_DIRECTORY, "passwords.json")

print("Passwords will be stored in:")
print(PASSWORD_FILE)

# 📂 Initialize password storage
def initialize_storage():

    if not os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "w") as file:
            json.dump({}, file)


# 🔑 Generate Strong Password
def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    return password


# 💾 Save Password
def save_password(service, password):

    try:
        with open(PASSWORD_FILE, "r") as file:
            data = json.load(file)
    except:
        data = {}

    data[service] = password

    with open(PASSWORD_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print(f"\n✅ Password saved for: {service}")


# 📂 View Saved Passwords
def view_passwords():

    try:
        with open(PASSWORD_FILE, "r") as file:
            data = json.load(file)
    except:
        print("\n⚠ No passwords stored yet.")
        return

    if len(data) == 0:
        print("\n⚠ No passwords stored yet.")
        return

    print("\n📂 Saved Passwords")
    print("============================")

    for service, password in data.items():
        print(f"{service} : {password}")


# 🚀 Main Menu
def main():

    initialize_storage()

    while True:

        print("\nChoose an option:")
        print("1️⃣ Generate new password")
        print("2️⃣ View saved passwords")
        print("3️⃣ Exit")

        choice = input("\nSelect option: ")

        # 🔑 Generate password
        if choice == "1":

            try:
                length = int(input("\nEnter password length (recommended 12+): "))
            except:
                print("Invalid input. Using default length: 12")
                length = 12

            password = generate_password(length)

            print("\n🔐 Generated Password:")
            print(password)

            save = input("\nDo you want to save this password? (y/n): ").lower()

            if save == "y":
                service = input("Enter service name (example: gmail, github): ")
                save_password(service, password)

        # 📂 View passwords
        elif choice == "2":
            view_passwords()

        # ❌ Exit
        elif choice == "3":
            print("\nExiting program...")
            break

        else:
            print("\nInvalid option. Try again.")


# ▶ Run program
if __name__ == "__main__":
    main()