import dns.resolver

def dns_lookup(domain):
    result = {}
    try:
        result["A"] = [str(a) for a in dns.resolver.resolve(domain, 'A')]
    except:
        result["A"] = []

    try:
        result["MX"] = [str(a) for a in dns.resolver.resolve(domain, 'MX')]
    except:
        result["MX"] = []

    try:
        result["NS"] = [str(a) for a in dns.resolver.resolve(domain, 'NS')]
    except:
        result["NS"] = []

    return result
