#!/usr/bin/env python3
"""
Fetchall fetches URLs in parallel and reports their times and sizes.
Python version using threads, queue, and httpx.
"""

import sys
import time
import threading
import queue
import httpx
from urllib.parse import urlparse


def fetch(url, result_queue):
    """Fetch a URL and put the result in the queue."""
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

    result_queue.put(result)


def main():
    if len(sys.argv) < 2:
        print('Usage: python fetchall.py <url1> [url2] [url3] ...')
        sys.exit(1)

    urls = sys.argv[1:]
    start_time = time.time()

    result_queue = queue.Queue()

    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch, args=(url, result_queue))
        thread.start()
        threads.append(thread)

    for _ in urls:
        result = result_queue.get()
        print(result)

    for thread in threads:
        thread.join()

    elapsed = time.time() - start_time
    print(f'{elapsed:.2f}s elapsed')


if __name__ == '__main__':
    main()
