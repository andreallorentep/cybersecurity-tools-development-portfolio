# Keylogger Simulator

A simple cybersecurity educational tool built in Python that simulates how a keylogger records keystrokes and generates session logs.

This tool is part of a Cybersecurity Tools Development Portfolio, demonstrating the basic concepts behind keystroke logging while emphasizing ethical cybersecurity practices and responsible use of monitoring technologies.

## Overview

The Keylogger Simulator records text entered by the user within the program and stores it in a structured log file.

Unlike real keyloggers, this tool does **not capture system-wide keystrokes** and only records input typed directly into the application. This makes it safe for learning while still demonstrating how keylogging mechanisms work internally.

The simulator helps cybersecurity learners understand:

- How keylogging mechanisms record input
- How activity logs are generated
- How session timestamps are stored
- How monitoring tools track user activity
- How forensic artifacts can be generated from user input logs

## Features

- Simulated keystroke logging
- Interactive command-line input capture
- Session-based logging
- Automatic timestamp recording
- Log file generation
- Safe educational implementation
- Ethical notice displayed at program startup

## Technologies Used

- Python 3
- os module
- datetime module
- File I/O operations
- Text-based logging system
- Command-line interface

## How It Works

The simulator works using a controlled input logging process:

1. The program starts and displays an ethical usage notice.
2. The user begins typing input into the console.
3. Each line of input is recorded as a simulated keystroke entry.
4. The program continues logging until the user types `exit`.
5. All captured input is stored in a list during the session.
6. When the session ends, the inputs are written to a log file.
7. A timestamped log file is generated containing the recorded entries.

## Example Output

Keylogger Simulator

Cybersecurity Educational Tool

ETHICAL NOTICE:

This tool is for educational purposes only.

It does NOT capture real system keystrokes.

Start typing (type 'exit' to stop):

> Hello  
Logged.

> cybersecurity  
Logged.

> exit

Session ended.

Keylog saved to: keylog_report.txt

## Output File

The tool generates a text-based log file:

keylog_report.txt

Example structure:

Keylogger Session  
Start Time: 2026-05-09 13:40:21

----------------------------------

Hello  
cybersecurity

----------------------------------

Session End

## Cybersecurity Relevance

Keylogging is a technique that can be used both legitimately and maliciously. Security professionals study keylogging behavior to understand how attackers capture sensitive information.

Keylogging techniques are commonly associated with:

- Credential theft malware
- Spyware infections
- Insider threat monitoring
- User activity auditing

Security analysts study keylogging behavior to learn how to:

- Detect suspicious monitoring software
- Identify credential harvesting malware
- Investigate user activity logs
- Perform forensic analysis of compromised systems

Understanding how keylogging works helps cybersecurity professionals develop better detection and mitigation strategies.

## Future Improvements

Possible enhancements for this project include:

- Real-time key event simulation
- Encrypted log storage
- Log integrity verification
- Session identifiers
- Log rotation system
- Integration with security monitoring dashboards

## Disclaimer

This tool is intended for educational and cybersecurity learning purposes only. It does not capture real system keystrokes and should never be used to monitor individuals without their knowledge and consent. Always ensure you have proper authorization before performing any monitoring or security testing.