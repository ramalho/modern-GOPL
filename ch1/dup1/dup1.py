#!/usr/bin/env python3
"""
Prints the text of each line that appears more than
once in the standard input, preceded by its count.
"""

import sys
from collections import Counter


def main():
    lines = [line.rstrip('\n') for line in sys.stdin]
    counts = Counter(lines)

    for line, n in counts.items():
        if n > 1:
            print(f'{n}\t{line}')


if __name__ == '__main__':
    main()
