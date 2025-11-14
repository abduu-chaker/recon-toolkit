import asyncio
from modules.subdomain_enum import subdomain_enum
from modules.port_scanner import port_scan
from modules.dir_bruteforce import dir_bruteforce
from modules.dns_resolver import dns_lookup

async def run_recon(target):
    print(f"[+] Starting Recon on: {target}")

    print("\n--- Subdomain Enumeration ---")
    subs = await subdomain_enum(target)
    print(f"Found {len(subs)} subdomains")

    print("\n--- Port Scanning ---")
    ports = await port_scan(target)
    print(f"Open ports: {ports}")

    print("\n--- DNS Lookup ---")
    dns_info = await dns_lookup(target)
    print(dns_info)

    print("\n--- Directory Bruteforce ---")
    dirs = await dir_bruteforce(target)
    print(f"Directories found: {dirs}")

    print("\n[+] Recon Finished!")
