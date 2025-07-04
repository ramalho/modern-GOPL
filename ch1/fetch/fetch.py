#!/usr/bin/env python3
"""
Fetch prints the content found at each specified URL.
Python translation of the Go program from:
The Go Programming Language by Alan A. A. Donovan & Brian W. Kernighan
"""

import sys
import httpx


def main():
    if len(sys.argv) < 2:
        print('Usage: python fetch.py <url1> [url2] ...', file=sys.stderr)
        sys.exit(1)

    for url in sys.argv[1:]:
        try:
            with httpx.Client() as client:
                response = client.get(url)
                response.raise_for_status()  # Raise exception for HTTP errors
                print(response.text, end='')
        except httpx.HTTPError as e:
            print(f'fetch: {e}', file=sys.stderr)
            sys.exit(1)


if __name__ == '__main__':
    main()
