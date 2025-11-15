import requests

def enumerate_subdomains(domain):
    print(f"[+] Enumerating subdomains for: {domain}")

    subdomains = [
        "www",
        "mail",
        "ftp",
        "dev",
        "test",
        "api",
        "staging",
        "admin"
    ]

    found = []

    for sub in subdomains:
        url = f"http://{sub}.{domain}"
        try:
            requests.get(url, timeout=2)
            print(f"  [+] Found: {sub}.{domain}")
            found.append(f"{sub}.{domain}")
        except:
            pass

    return found

if __name__ == "__main__":
    d = input("Enter domain: ")
    res = enumerate_subdomains(d)
    print("\n[+] Subdomains Found:")
    for r in res:
        print(" -", r)
