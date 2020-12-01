#!/usr/bin/env python3
"""tests for cougar_test.py"""

import os
from subprocess import getstatusoutput, getoutput

#MAB: making it so that can pass any file to test_exists

# --------------------------------------------------
def test_exists(data):
    """exists"""
    
    assert os.path.isfile(data)

#test_exists('./cougar_test.py')

# --------------------------------------------------
def test_runnable(data):
    """Runs using python3"""

    out = getoutput(f'python3 {data}')
    assert out.strip() == 'Python3 Enabled'

#test_runnable('./cougar_test.py')
    
# --------------------------------------------------
def test_executable():
    #"""Says 'Hello, World!' by default"""

    #out = getoutput(prg)
    #assert out.strip() == 'Hello, World!'


# --------------------------------------------------
def test_usage():
    """usage"""

   # for flag in ['-h', '--help']:
   #     rv, out = getstatusoutput(f'{prg} {flag}')
   #     assert rv == 0
   #     assert out.lower().startswith('usage')


# --------------------------------------------------
def test_input():
    """test for input"""

   # for val in ['Universe', 'Multiverse']:
   #     for option in ['-n', '--name']:
   #         rv, out = getstatusoutput(f'{prg} {option} {val}')
   #         assert rv == 0
   #         assert out.strip() == f'Hello, {val}!'
