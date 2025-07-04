#!/usr/bin/env python3

"""
Echo3 prints its command-line arguments.
"""

import sys


def main():
    print(' '.join(sys.argv[1:]))


if __name__ == '__main__':
    main()
