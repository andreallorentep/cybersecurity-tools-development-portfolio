# 🔐 File Integrity Checker
# Cybersecurity Portfolio Project

import hashlib
import os
import json
from datetime import datetime

print("===================================")
print(" File Integrity Checker")
print(" Cybersecurity Monitoring Tool")
print("===================================\n")

# 🎯 Target file
file_path = input("Enter the file path to monitor: ")

# 📊 Results storage
results = {
    "target_file": file_path,
    "scan_time": str(datetime.now()),
    "original_hash": "",
    "new_hash": "",
    "status": ""
}

# 🧠 Function to calculate file hash
def calculate_hash(path):

    sha256 = hashlib.sha256()

    try:
        with open(path, "rb") as file:

            while True:
                block = file.read(4096)

                if not block:
                    break

                sha256.update(block)

        return sha256.hexdigest()

    except Exception as e:
        print(f"Error reading file: {e}")
        return None


# 🚀 Initial hash calculation
print("\n[+] Calculating original file hash...\n")

original_hash = calculate_hash(file_path)

if original_hash is None:
    print("File could not be read.")
    exit()

results["original_hash"] = original_hash

print("Original Hash:")
print(original_hash)

# ⏳ Wait for modification
input("\nModify the file if you want to test integrity and press ENTER...\n")

# 🔎 Recalculate hash
print("[+] Recalculating file hash...\n")

new_hash = calculate_hash(file_path)

results["new_hash"] = new_hash

print("New Hash:")
print(new_hash)

# ⚠️ Integrity verification
if original_hash == new_hash:

    results["status"] = "SAFE"

    print("\n[✔] File integrity verified.")
    print("The file has NOT been modified.")

else:

    results["status"] = "ALERT"

    print("\n[⚠] WARNING: File modification detected!")
    print("The file hash has changed.")

# 💾 Save report
output_file = "integrity_report.json"

with open(output_file, "w") as report:
    json.dump(results, report, indent=4)

print(f"\nReport saved to: {output_file}")