# 🧰 Keylogger Lab
# Cybersecurity Detection Tool

import os
import datetime

# 📂 List to store captured input
log_entries = []

# 🖥️ Program Header
print("===================================")
print(" Keylogger Simulator")
print(" Cybersecurity Educational Tool")
print("===================================")

# ⚠️ Ethical notice
print("\n⚠️ ETHICAL NOTICE")
print("This tool is for educational purposes only.")
print("It does NOT capture real system keystrokes.")
print("It only logs text typed inside this program.")

# ⌨️ Start simulated key logging
print("\n⌨️ Start typing (type 'exit' to stop):\n")

while True:

    user_input = input("> ")

    if user_input.lower() == "exit":
        break

    # 🕒 Timestamp for each entry
    timestamp = datetime.datetime.now()

    # 📝 Store log entry
    log_entries.append(f"[{timestamp}] {user_input}")

    print("Logged.")

# 🛑 End of session
print("\nSession ended.")

# 📁 Get script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# 📄 Create log file path
log_file_path = os.path.join(script_directory, "keylog_report.txt")

# 💾 Save log entries to file
with open(log_file_path, "w") as file:

    for entry in log_entries:
        file.write(entry + "\n")

# ✅ Confirmation message
print(f"\n📄 Keylog saved to: {log_file_path}")