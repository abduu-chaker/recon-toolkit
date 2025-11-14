import aiohttp
import asyncio

async def fetch(session, url):
    try:
        async with session.get(url, timeout=4) as response:
            if response.status == 200:
                return url
    except:
        return None

async def subdomain_enum(domain):
    subdomains = ["www", "api", "mail", "dev", "test", "admin", "cpanel"]
    found = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for sub in subdomains:
            url = f"http://{sub}.{domain}"
            tasks.append(fetch(session, url))

        results = await asyncio.gather(*tasks)
        for r in results:
            if r:
                found.append(r)

    return found
