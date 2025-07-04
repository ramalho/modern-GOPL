#!/usr/bin/env python3
"""
Prints the count and text of lines that appear more than once
in the input. It reads from stdin or from a list of named files.
"""

import fileinput
from collections import Counter


def main() -> None:
    counts = Counter()

    for line in fileinput.input():
        line = line.rstrip('\n')
        counts[line] += 1

    for line, n in counts.items():
        if n > 1:
            print(f'{n}\t{line}')


if __name__ == '__main__':
    main()
