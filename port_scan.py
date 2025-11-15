import socket

def scan_ports(target):
    print(f"[+] Scanning ports for: {target}")

    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        139: "SMB",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        3389: "RDP"
    }

    open_ports = []

    for port, name in common_ports.items():
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            print(f"  [+] Open: {port} ({name})")
            open_ports.append((port, name))

        s.close()

    return open_ports


if __name__ == "__main__":
    t = input("Enter IP or domain: ")
    res = scan_ports(t)
    print("\n[+] Open Ports Found:")
    for p, n in res:
        print(f" - {p} ({n})")
