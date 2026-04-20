# Simple Firewall

## Overview
This project is a Python-based simple firewall that monitors network traffic in real time and blocks packets from specific ports. It demonstrates fundamental network security concepts such as packet inspection and traffic filtering.

The firewall captures packets from the network interface and analyzes their destination ports. If a packet is detected using a blocked port, the firewall identifies it and prevents it from being allowed through the monitoring system.

This project demonstrates how packet filtering works at a basic level and how security tools can monitor network activity to detect potentially dangerous traffic.

## Features
- Real-time packet monitoring
- Detection of traffic from blocked ports
- Customizable list of blocked ports
- Command-line interface output
- Packet inspection using Scapy

## Technologies Used
- Python
- Scapy
- Npcap (required on Windows)

## How It Works
The program captures live network packets using Scapy.

1. The firewall listens for incoming packets on the network interface.
2. Each packet is inspected to determine if it contains TCP or UDP traffic.
3. The destination port is extracted from the packet.
4. If the destination port matches one of the blocked ports, the firewall flags the packet as blocked.

Example output:

===================================
 🔥 Simple Firewall
 Real-Time Packet Filtering System
===================================

Blocked ports: [23, 445]

[+] Firewall is running... Listening for traffic...

[BLOCKED] Packet detected on blocked port: 23
[BLOCKED] Packet detected on blocked port: 445

## Installation

1. Install Python 3.

2. Install Scapy:

pip install scapy

3. Install Npcap (required for packet capture on Windows).

Download it from:
https://npcap.com/

## Usage

Run the firewall from the terminal:

python simple_firewall.py

The program will start monitoring network traffic and will notify when packets are detected on blocked ports.

## Disclaimer
This tool is intended for educational purposes and for use on networks you own or have permission to test.