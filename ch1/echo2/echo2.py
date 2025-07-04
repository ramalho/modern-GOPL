#!/usr/bin/env python3
"""
Echo2 prints its command-line arguments.
"""

import sys


def main():
    s, sep = '', ''
    for arg in sys.argv[1:]:
        s += sep + arg
        sep = ' '
    print(s)


if __name__ == '__main__':
    main()
