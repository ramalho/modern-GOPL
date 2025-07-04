#!/usr/bin/env python3
"""
Prints the count and text of lines that appear more than once
in the input. It reads from stdin or from a list of named files.
"""

import sys
from collections import Counter
from typing import TextIO


def main() -> None:
    counts = Counter()
    files = sys.argv[1:]

    if len(files) == 0:
        count_lines(sys.stdin, counts)
    else:
        for filename in files:
            try:
                with open(filename, 'r') as f:
                    count_lines(f, counts)
            except IOError as err:
                print(f'dup2: {err}', file=sys.stderr)
                continue

    for line, n in counts.items():
        if n > 1:
            print(f'{n}\t{line}')


def count_lines(f: TextIO, counts: Counter[str]) -> None:
    """Count lines from a file object and update the Counter."""
    for line in f:
        line = line.rstrip('\n')
        counts[line] += 1


if __name__ == '__main__':
    main()
