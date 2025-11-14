import asyncio
import socket

async def check_port(host, port):
    try:
        conn = asyncio.open_connection(host, port)
        reader, writer = await asyncio.wait_for(conn, timeout=1)
        writer.close()
        return port
    except:
        return None

async def port_scan(host):
    ports_to_check = [80, 443, 22, 21, 8080, 3306]
    tasks = [check_port(host, p) for p in ports_to_check]
    results = await asyncio.gather(*tasks)
    return [p for p in results if p]
