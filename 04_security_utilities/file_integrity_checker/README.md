# File Integrity Checker

## Overview
This project is a Python-based **educational file integrity monitoring tool** designed to detect **unauthorized modifications in files** using cryptographic hash functions.

The tool calculates a **SHA-256 hash** of a file to generate a baseline fingerprint. It then recalculates the hash after a potential modification and compares the results to determine whether the file has changed.

This project demonstrates how **File Integrity Monitoring (FIM)** systems work and provides insight into techniques used by **Host-based Intrusion Detection Systems (HIDS)** to detect unauthorized changes in system files.

## Features
- File integrity verification using **SHA-256 hashing**
- Detection of unauthorized file modifications
- Hash comparison for integrity validation
- Interactive monitoring process
- Structured security report generation (JSON output)
- Timestamped integrity checks
- Simple command-line interface
- Local file report generation

## Technologies Used
- Python
- hashlib library
- json module
- os module
- datetime module
- File system operations
- Cryptographic hashing

## How It Works
The integrity checker verifies whether a file has been modified by comparing cryptographic hashes.

1. The user provides the path of the file to monitor.
2. The program calculates the **original SHA-256 hash** of the file.
3. The user is given the opportunity to modify the file.
4. The program recalculates the hash of the file.
5. The two hashes are compared.
6. If the hashes differ, the tool reports a **file integrity violation**.
7. All results are saved in a structured **JSON report**.

This process simulates how real-world **file integrity monitoring systems** detect unauthorized changes in critical system files.

## Example Output
File Integrity Checker
Cybersecurity Monitoring Tool

Enter the file path to monitor: test.txt

[+] Calculating original file hash...

Original Hash:
52c237b919697b71519629a02bcfdbabad8e9327c944ba574f150bfdd223695c

Modify the file if you want to test integrity and press ENTER...

[+] Recalculating file hash...

New Hash:
48a781cfd96c121b25ac63c902497741841b78166097d0316f72a62f46552e3a

[⚠] WARNING: File modification detected!
The file hash has changed.

Report saved to: integrity_report.json

Scan completed.

## Output File
The integrity checker generates a structured report file:
integrity_report.json

Example structure:
{
    "target_file": "test.txt",
    "scan_time": "2026-05-03 11:20:00",
    "original_hash": "52c237b919697b71519629a02bcfdbabad8e9327c944ba574f150bfdd223695c",
    "new_hash": "48a781cfd96c121b25ac63c902497741841b78166097d0316f72a62f46552e3a",
    "status": "ALERT"
}

## Installation

Clone the repository or download the project.

Run the tool using Python:
python file_integrity_checker.py

No external dependencies are required because the program uses only Python's standard libraries.

## Disclaimer

This tool is intended for educational purposes and for use on systems or files that you own or have permission to monitor.
Unauthorized monitoring or modification detection on systems without proper authorization may violate security policies or laws.