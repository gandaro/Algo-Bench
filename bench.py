#!/usr/bin/env python

import sys

from glob import glob
from math import factorial
from timeit import Timer
from argparse import ArgumentParser

MODULES = ['enterprise_programmer', 'expert_programmer', 'firstyear_c',
           'firstyear_pascal', 'firstyear_python', 'firstyear_sicp',
           'gandaro', 'lazier_python', 'lazy_python', 'newbie',
           'python_expert', 'python_hacker', 'unix_programmer',
           'windows_programmer']

global function, args

def bench(name, result):
    if function(*args) != result:
        print >>sys.stderr, 'Fail!  "%s" failed!' % name
        return 0

    return Timer('function(*args)',
                 'from __main__ import function, args').timeit(20)/20


if __name__ == '__main__':
    p = ArgumentParser(description='Benchmark factorial algorithms.')
    p.add_argument('--number', '-n', type=int, default=5000,
                   help='Number to calculate its factorial.', required=False)
    r = p.parse_args().number

    sys.setrecursionlimit(r * 2)
    correct = factorial(r)
    args = [r]

    for x in MODULES:
        print '#', x

        try:
            m = __import__('algos.%s' % x, fromlist=['factorial'])
            function = m.factorial
            print bench(m.__name__, correct), 'seconds.'

        except Exception as e:
            print >>sys.stderr, 'ERROR:', e.message

        print
