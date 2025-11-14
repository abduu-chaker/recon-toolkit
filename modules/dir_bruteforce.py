import aiohttp
import asyncio

async def brute(session, url):
    try:
        async with session.get(url, timeout=4) as r:
            if r.status not in [404]:
                return url
    except:
        return None

async def dir_bruteforce(domain):
    wordlist = ["admin", "login", "uploads", "dashboard", "api", "images"]
    found = []

    async with aiohttp.ClientSession() as session:
        tasks = []
        for path in wordlist:
            url = f"http://{domain}/{path}/"
            tasks.append(brute(session, url))

        results = await asyncio.gather(*tasks)
        for r in results:
            if r:
                found.append(r)

    return found
