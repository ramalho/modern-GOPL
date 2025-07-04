#!/usr/bin/env python3

import sys
import time
import asyncio
import httpx
from urllib.parse import urlparse


async def fetch(url, client):
    start = time.time()
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'http://' + url

        response = await client.get(url)
        response.raise_for_status()

        nbytes = len(response.content)

        elapsed = time.time() - start
        result = f'{elapsed:.2f}s {nbytes:7d} {url}'

    except httpx.HTTPError as e:
        result = f'Error fetching {url}: {e}'
    except Exception as e:
        result = f'Unexpected error with {url}: {e}'

    return result


async def main():
    if len(sys.argv) < 2:
        print('Usage: python fetchall.py <url1> [url2] [url3] ...')
        return

    urls = sys.argv[1:]
    start_time = time.time()

    async with httpx.AsyncClient(timeout=30.0) as client:
        tasks = [fetch(url, client) for url in urls]

        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)

    elapsed = time.time() - start_time
    print(f'{elapsed:.2f}s elapsed')


if __name__ == '__main__':
    asyncio.run(main())
