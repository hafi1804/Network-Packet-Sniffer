from scapy.all import sniff, IP, TCP, UDP, ICMP

print("=== Network Packet Sniffer ===")
print("Capturing packets...\n")

def packet_callback(packet):

    if packet.haslayer(IP):

        src = packet[IP].src
        dst = packet[IP].dst
        length = len(packet)

        if packet.haslayer(TCP):
            protocol = "TCP"

        elif packet.haslayer(UDP):
            protocol = "UDP"

        elif packet.haslayer(ICMP):
            protocol = "ICMP"

        else:
            protocol = "Other"

        print(f"Source: {src}")
        print(f"Destination: {dst}")
        print(f"Protocol: {protocol}")
        print(f"Length: {length} bytes")
        print("-" * 50)

sniff(prn=packet_callback, store=False)