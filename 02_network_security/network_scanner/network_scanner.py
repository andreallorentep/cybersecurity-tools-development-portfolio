# Network Scanner
# Cybersecurity Portfolio Project

import socket
import ipaddress
import subprocess
from concurrent.futures import ThreadPoolExecutor

# 🚪Puertos comunes
PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389]

# 🌐 Get local IP address
def get_local_ip():
    s =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# 🧠 Calculate network range
def get_network(ip):
    return ipaddress.ip_network(ip + "/24", strict=False)

# 📡 Check if host is alive     
def ping_host(ip):
    try:
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "100", ip],
            stdout=subprocess.DEVNULL
        )
        if result.returncode == 0:
            return ip
    except:
        pass
    return None

# 🚪 Check if a port is open
def scan_port(ip, port):
    s = socket.socket()
    s.settimeout(0.3)
    
    try:
        s.connect((ip, port))
        print(f"    [OPEN PORT] {port}")
    except:    
        pass
    finally:
        s.close()

# 🔎 Scan a single host
def scan_host(ip):
    live = ping_host(ip)

    if live:
        print(f"\n[LIVE] {ip}")

        for port in PORTS:
            scan_port(ip, port)

# 🧠 Main program
def main():
    
    print("="*40)
    print(" Network Scanner")
    print("="*40)

    local_ip = get_local_ip()
    print(f"\nLocal IP: {local_ip}")

    base_ip = ".".join(local_ip.split(".")[:3])

    print("\nScanning network...\n")

    with ThreadPoolExecutor(max_workers=100) as executor:
       
        for i in range(1, 255):
            ip = f"{base_ip}.{i}"
            executor.submit(scan_host, ip)

# 🚀 Entry point
if __name__ == "__main__":
    main()