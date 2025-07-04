#!/usr/bin/env python3

"""
Echo1 prints its command-line arguments.
"""

import sys


def main():
    s = ''
    sep = ''
    for i in range(1, len(sys.argv)):
        s += sep + sys.argv[i]
        sep = ' '
    print(s)


if __name__ == '__main__':
    main()
