# 🌐 WHOIS Lookup Tool
# Cybersecurity Reconnaissance Utility

import whois
import json
import os
from datetime import datetime

print("===================================")
print(" WHOIS Lookup Tool")
print(" Cybersecurity Recon Utility")
print("===================================\n")

# 🎯 Target Domain
domain = input("Enter domain to investigate (example: google.com): ")

# 📊 Results storage
results = {
    "domain": domain,
    "lookup_time": str(datetime.now()),
    "registrar": "",
    "creation_date": "",
    "expiration_date": "",
    "name_servers": "",
    "status": ""
}

# 🔎 Perform WHOIS Lookup
def perform_whois_lookup(target):

    try:
        info = whois.whois(target)

        results["registrar"] = str(info.registrar)
        results["creation_date"] = str(info.creation_date)
        results["expiration_date"] = str(info.expiration_date)
        results["name_servers"] = str(info.name_servers)

        return info

    except Exception as e:
        print("Error performing WHOIS lookup:", e)
        return None


# 🧠 Basic Legitimacy Check
def legitimacy_check(info):

    if info is None:
        results["status"] = "ERROR"
        return

    creation = str(info.creation_date)

    if "2025" in creation or "2026" in creation:
        results["status"] = "⚠ Potentially New Domain (Investigate Further)"
    else:
        results["status"] = "Likely Established Domain"


# 🚀 Run lookup
print("\n[+] Performing WHOIS lookup...\n")

info = perform_whois_lookup(domain)

# 🧠 Analyze legitimacy
legitimacy_check(info)

# 📊 Display Results
print("\n===== WHOIS REPORT =====\n")

print("Domain:", results["domain"])
print("Registrar:", results["registrar"])
print("Creation Date:", results["creation_date"])
print("Expiration Date:", results["expiration_date"])
print("Name Servers:", results["name_servers"])
print("Status:", results["status"])

# 💾 Save report
output_file = "whois_report.json"

with open(output_file, "w") as f:
    json.dump(results, f, indent=4)

print("\nReport saved to:", os.path.abspath(output_file))