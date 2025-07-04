#!/usr/bin/env python3
"""
Dup3 prints the count and text of lines that
appear more than once in the named input files.
"""

import sys
from collections import Counter


def main(filenames: list[str]) -> None:
    counts = Counter()

    for filename in filenames:
        try:
            with open(filename, 'r') as f:
                data = f.read()
        except IOError as err:
            print(f'dup3: {err}', file=sys.stderr)
            continue

        counts.update(data.split('\n'))

    for line, n in counts.items():
        if n > 1:
            print(f'{n}\t{line}')


if __name__ == '__main__':
    main(sys.argv[1:])
