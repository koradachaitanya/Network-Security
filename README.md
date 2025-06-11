Certainly! Here is a professional README file describing both the **Port Scanning** and **Basic Vulnerability Scanning with Nmap** tasks:

---

# Network Security Tasks: Port Scanning & Vulnerability Scanning

## Overview

This project demonstrates two foundational network security tasks:

1. **Simple Port Scanning using Python's socket library**
2. **Basic Vulnerability Scanning using Nmap automated with Python's subprocess module**

These scripts help identify open ports and potential vulnerabilities on a target system, providing essential skills for network reconnaissance and security assessment.

---

## Task 1: Simple Port Scanning

### Description

Port scanning is a technique used to discover which network ports on a target machine are open and accepting connections. Open ports can indicate running services and potential entry points for attackers.

### How It Works

- The script iterates over a specified range of TCP ports on a target host.
- For each port, it attempts to establish a TCP connection using Python’s `socket` library.
- If the connection is successful, the port is reported as open.

### Features

- Scans a user-defined range of ports (e.g., 20–1024)
- Reports all open ports on the target
- Simple and fast for small-to-medium port ranges

---

## Task 2: Basic Vulnerability Scanning with Nmap

### Description

Vulnerability scanning goes beyond port scanning by probing open ports for known security issues. This task automates the use of [Nmap](https://nmap.org/)—a popular network scanning tool—using Python’s `subprocess` module.

### How It Works

- The script runs various Nmap commands via `subprocess`, including:
  - Basic port scanning
  - Service/version detection
  - OS detection
  - Vulnerability scanning using Nmap Scripting Engine (NSE)
- Results are printed to the console for review.

### Features

- Automates multiple Nmap scan types from a single Python script
- Checks for common vulnerabilities (e.g., SMB, HTTP, SSL Heartbleed)
- Outputs comprehensive scan results for analysis

---

## Requirements

- Python 3.x
- Nmap (must be installed and available in your system PATH)
- (Optional) `pip install nmap` for advanced scripting

---

## How to Run

1. **Clone the repository or download the scripts.**
2. **Install Nmap** on your system ([Download Nmap](https://nmap.org/download.html)).
3. **Run the Python scripts** in your terminal:
   - For port scanning: `python port_scanner.py`
   - For Nmap vulnerability scanning: `python nmap_vuln_scan.py`
4. **Review the output** in your terminal.

---

## Disclaimer

- **Use these scripts only on systems you own or have explicit permission to test.**
- Unauthorized scanning of networks or devices is illegal and unethical.

---

## License

This project is for educational purposes only.

---

**Created by Korada Chaitanya**  

---
