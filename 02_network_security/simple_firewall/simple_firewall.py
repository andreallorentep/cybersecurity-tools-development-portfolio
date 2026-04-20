# Simple Firewall
# Cybersecurity Portfolio Project

from scapy.all import sniff, IP, TCP

# 🚫 Blocked ports
BLOCKED_PORTS = [23, 445]

# 🎯 Ports we care about (security relevant)
WATCH_PORTS = [21, 23, 80, 443, 445, 3389]

# 🧠 Store already seen connections
seen_connections = set()


def process_packet(packet):
    try:
        if packet.haslayer(IP) and packet.haslayer(TCP):

            src_ip = packet[IP].src
            dst_ip = packet[IP].dst
            dest_port = packet[TCP].dport

            connection = (src_ip, dst_ip, dest_port)

            # Ignore duplicates
            if connection in seen_connections:
                return

            seen_connections.add(connection)

            # Only show interesting ports
            if dest_port in WATCH_PORTS:

                print(f"\n[TRAFFIC]")
                print(f"Source: {src_ip}")
                print(f"Destination: {dst_ip}")
                print(f"Port: {dest_port}")

                if dest_port in BLOCKED_PORTS:
                    print("❌ BLOCKED by firewall rule")
                else:
                    print("✅ ALLOWED")

    except Exception as e:
        print(f"Error: {e}")


print("===================================")
print(" 🔥 Simple Firewall")
print(" Real-Time Packet Filtering System")
print("===================================\n")

print(f"Blocked ports: {BLOCKED_PORTS}")
print("\n[+] Firewall is running...\n")

sniff(prn=process_packet, store=0)