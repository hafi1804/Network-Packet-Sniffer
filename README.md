# Network Packet Sniffer

## Project Overview

The Network Packet Sniffer is a Python-based network monitoring tool designed to capture and analyze packets transmitted across a network interface in real time. The project utilizes the Scapy library to inspect network traffic and extract essential packet information such as source IP address, destination IP address, protocol type, and packet length.

This project provides a practical introduction to network traffic analysis and packet inspection, helping users understand how data is transmitted over computer networks.

---

## Project Scope

The scope of this project includes:

* Real-time packet capture and monitoring.
* Identification of source and destination IP addresses.
* Detection of common network protocols such as TCP, UDP, and ICMP.
* Display of packet size information.
* Basic network traffic analysis for educational purposes.
* Demonstration of packet sniffing concepts used in cybersecurity and network administration.

### Limitations

* Captures only basic packet information.
* Does not perform deep packet inspection.
* Does not store captured packets for later analysis.
* Does not include graphical visualization features.
* Requires appropriate permissions to capture network traffic.

---

## Technologies Used

* Python 3
* Scapy Library

---

## Features

* Captures network packets in real time.
* Displays source and destination IP addresses.
* Identifies TCP, UDP, and ICMP protocols.
* Shows packet length in bytes.
* Lightweight command-line interface.
* Continuous monitoring until manually stopped.

---

## Working Principle

1. The program starts packet capture on the active network interface.
2. Each captured packet is analyzed using the Scapy library.
3. The source IP address is extracted.
4. The destination IP address is extracted.
5. The protocol type (TCP, UDP, ICMP, or Other) is identified.
6. Packet size information is displayed.
7. The captured packet details are printed in real time.

---

## Information Captured

The packet sniffer displays:

* Source IP Address
* Destination IP Address
* Protocol Type
* Packet Length

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd network-packet-sniffer
```

3. Install the required dependency:

```bash
pip install scapy
```

---

## Usage

Run the program using:

```bash
python packet_sniffer.py
```

The application will begin capturing packets immediately.

To stop packet capture, press:

```text
Ctrl + C
```

---

## Sample Output

```text
=== Network Packet Sniffer ===
Capturing packets...

Source: 192.168.1.10
Destination: 142.250.183.78
Protocol: TCP
Length: 60 bytes
--------------------------------------------------

Source: 192.168.1.10
Destination: 8.8.8.8
Protocol: UDP
Length: 74 bytes
--------------------------------------------------
```

---

## Educational Objective

The primary objective of this project is to understand:

* Fundamentals of computer networking.
* Packet capture and packet analysis techniques.
* Network communication protocols.
* Real-time traffic monitoring.
* Basic cybersecurity monitoring concepts.
* Usage of Scapy for network security applications.

---

## Applications

* Network Traffic Monitoring
* Cybersecurity Education
* Protocol Analysis
* Network Troubleshooting
* Security Research
* Learning Packet Inspection Techniques

---

## Disclaimer

This project is intended solely for educational and authorized network monitoring purposes. Users must ensure they have permission to capture and analyze network traffic. Unauthorized monitoring of network communications may violate legal, ethical, or organizational policies.

---

## Author

M Hafiza **Intern ID:** CITS1108 **Project:** SQL Injection Vulnerability Scanner **Duration:** 8 Weeks
