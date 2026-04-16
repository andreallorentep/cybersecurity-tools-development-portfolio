# Network Scanner

## Overview
This project is a Python-based network scanner that identifies active devices on a local network and checks for open ports on those devices. It demonstrates fundamental network security concepts such as host discovery and TCP port scanning.

The tool scans the local `/24` network range, detects live hosts using ICMP ping requests, and attempts TCP connections on common ports to determine whether they are open.

## Features
- Discover active devices on a local network
- Scan common TCP ports on detected hosts
- Multithreaded scanning for faster performance
- Command-line interface output
- Automatic detection of the local network range

## Technologies Used
- Python
- socket module
- subprocess module
- ipaddress module
- concurrent.futures (multithreading)

## How It Works
The program first determines the local IP address and calculates the corresponding `/24` network range.

1. The scanner sends ICMP ping requests to identify live hosts.
2. For each active device, it attempts to establish a TCP connection to a list of common ports.
3. If the connection succeeds, the port is reported as open.
4. Multithreading allows the scanner to analyze multiple hosts simultaneously, significantly reducing the scanning time.

Example output:
[LIVE] 192.168.0.1
[OPEN PORT] 22
[OPEN PORT] 53
[OPEN PORT] 80

[LIVE] 192.168.0.169
[OPEN PORT] 443
[OPEN PORT] 139
[OPEN PORT] 445

## Installation

No external dependencies are required.

Run the scanner using Python:

```bash
python network_scanner.py