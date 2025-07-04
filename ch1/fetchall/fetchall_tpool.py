#!/usr/bin/env python3

import sys
import time
import httpx
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor


def fetch(url):
    start = time.time()
    try:
        parsed = urlparse(url)
        if not parsed.scheme:
            url = 'http://' + url

        with httpx.Client(timeout=30.0) as client:
            response = client.get(url)
            response.raise_for_status()

            nbytes = len(response.content)

        elapsed = time.time() - start
        result = f'{elapsed:.2f}s {nbytes:7d} {url}'

    except httpx.HTTPError as e:
        result = f'Error fetching {url}: {e}'
    except Exception as e:
        result = f'Unexpected error with {url}: {e}'

    return result


def main():
    if len(sys.argv) < 2:
        print('Usage: python fetchall.py <url1> [url2] [url3] ...')
        return

    urls = sys.argv[1:]
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        results = list(executor.map(fetch, urls))

        for result in results:
            print(result)

    elapsed = time.time() - start_time
    print(f'{elapsed:.2f}s elapsed')


if __name__ == '__main__':
    main()
