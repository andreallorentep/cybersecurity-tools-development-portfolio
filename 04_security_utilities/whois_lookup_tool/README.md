# WHOIS Lookup Tool

A simple cybersecurity reconnaissance utility built in Python that performs WHOIS lookups on domains and generates structured investigation reports.

This tool is designed as part of a **Cybersecurity Tools Development Portfolio**, demonstrating basic recon techniques used during the information gathering phase of security assessments.

## Overview

The WHOIS Lookup Tool allows users to investigate domain registration information. It retrieves publicly available WHOIS data and presents it in a readable format while also saving the results to a JSON report file.

This tool can help security analysts identify:

- Domain registration details
- Domain creation and expiration dates
- Name servers associated with the domain
- Registrar information
- Domain maturity (new vs established domains)

## Features

- Perform WHOIS lookups for any domain
- Extract registrar information
- Identify domain creation and expiration dates
- List associated name servers
- Classify domains as **New** or **Established**
- Automatically generate a **JSON report**

## Technologies Used

- Python 3
- `python-whois` library
- JSON for structured reporting
- Virtual environment (`venv`)

## Installation

Clone the repository or download the project.

git clone https://github.com/yourusername/whois_lookup_tool.git
cd whois_lookup_tool

Install the required dependency:
pip install python-whois

## Example output
===== WHOIS REPORT =====

Domain: google.com
Registrar: MarkMonitor, Inc.
Creation Date: 1997-09-15
Expiration Date: 2028-09-14
Name Servers:
 - NS1.GOOGLE.COM
 - NS2.GOOGLE.COM
 - NS3.GOOGLE.COM
 - NS4.GOOGLE.COM
Status: Likely Established Domain

The report will also be saved as:
whois_report.json

## Example JSON Report
{
  "domain": "google.com",
  "registrar": "MarkMonitor, Inc.",
  "creation_date": "1997-09-15",
  "expiration_date": "2028-09-14",
  "name_servers": [
    "NS1.GOOGLE.COM",
    "NS2.GOOGLE.COM",
    "NS3.GOOGLE.COM",
    "NS4.GOOGLE.COM"
  ],
  "status": "Likely Established Domain"
}

## Cybersecurity Relevance

WHOIS analysis is commonly used during the reconnaissance phase of:

Penetration testing
Threat intelligence
OSINT investigations
Phishing infrastructure analysis
Domain reputation assessment

Security analysts often use WHOIS data to detect:

Newly registered suspicious domains
Potential phishing infrastructure
Domain ownership patterns

## Future Improvements

Possible enhancements for this tool include:

DNS record lookup
Domain IP resolution
Subdomain discovery
WHOIS history tracking
Integration with threat intelligence APIs

## Disclaimer

This tool is intended for educational and cybersecurity research purposes only. Always ensure you have permission before performing security assessments.