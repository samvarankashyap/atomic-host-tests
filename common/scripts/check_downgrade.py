#!/usr/bin/env python

from __future__ import print_function
from distutils.version import LooseVersion
import re
import sys


def warn_downgrade(msg):
    print("WARN: Possible downgrade detected! ", msg, file=sys.stderr)


def check_downgrade(line):
    '''
    Tests to see if the line has the correct amount of words and then does
    a version compare to determine if a package was downgraded.

    Looking for lines like this:

    kernel 3.10.0-229.14.1.el7 -> 3.10.0-324.el7
    '''
    rc = 0
    words = line.split()
    if len(words) != 4:
        pass
    elif LooseVersion(words[1]) > LooseVersion(words[3]):
        warn_downgrade(line.strip())
        rc = 1

    return rc


def main():
    exit_status = 0
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("ERR: Need to supply filename!", file=sys.stderr)
        sys.exit(1)

    with open(filename, 'r') as f:
        for l in f:
            # check if the line starts with 2 spaces
            if re.search('^  ', l):
                if check_downgrade(l):
                    exit_status = 1
            else:
                pass

    sys.exit(exit_status)

if __name__ == "__main__":
    main()
