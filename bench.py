#!/usr/bin/env python

import sys
import os.path

from glob import glob
from math import factorial
from timeit import Timer

MODULES = ['enterprise_programmer', 'expert_programmer', 'firstyear_c',
           'firstyear_pascal', 'firstyear_python', 'firstyear_sicp',
           'gandaro', 'lazier_python', 'lazy_python', 'newbie',
           'python_expert', 'python_hacker', 'unix_programmer',
           'windows_programmer']

def bench(name, result, function, *args):
    if function(*args) != result:
        print >>sys.stderr, 'Fail!  "%s" failed!' % name
        return 0

    return Timer('function(*args)',
                 'from __main__ import function, args').timeit(20)/20


if __name__ == '__main__':
    try:
        r = sys.argv[1]
    except IndexError:
        r = 5000

    global args
    args = [r]

    sys.setrecursionlimit(r * 2)

    correct = factorial(r)

    for x in MODULES:
        print ':::::::', x, ':::::::'
        try:
            m = __import__('algos.%s' % x, fromlist=['factorial'])
            global function
            function = m.factorial
            print bench(m.__name__, correct, function, r), 'seconds.'
        except Exception as e:
            print >>sys.stderr, 'ERROR:', e.message
