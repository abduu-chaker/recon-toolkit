import json
from subdomain_enum import enumerate_subdomains
from port_scan import scan_ports

def save_report(data):
    with open("report.json", "w") as f:
        json.dump(data, f, indent=4)
    print("\n[+] JSON report saved as report.json")

def main():
    print("""
====================================
   RECON TOOLKIT - MAIN MENU
====================================

1) Subdomain Enumeration
2) Port Scanning
3) Run Full Scan (Subdomains + Ports)
0) Exit

====================================
""")

    choice = input("Choose an option: ")

    if choice == "1":
        domain = input("Enter domain: ")
        subs = enumerate_subdomains(domain)
        data = {"domain": domain, "subdomains": subs}
        save_report(data)

    elif choice == "2":
        target = input("Enter IP or domain: ")
        ports = scan_ports(target)
        data = {"target": target, "open_ports": ports}
        save_report(data)

    elif choice == "3":
        domain = input("Enter domain for full scan: ")

        print("\n[+] Running subdomain enumeration...")
        subs = enumerate_subdomains(domain)

        print("\n[+] Running port scan...")
        ports = scan_ports(domain)

        data = {
            "domain": domain,
            "subdomains": subs,
            "open_ports": ports
        }

        save_report(data)

    elif choice == "0":
        print("Exiting...")
        return

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
