
""" Data Wrangler Automation """
""" Author: Neeka Sewnath """

import argparse
import os

def get_args() -> Args:
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Data Wrangler Automation',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    if os.path.isfile(args.data):
        args.data = open(args.data).read().rstrip()

    return Args(args.data)

# --------------------------------------------------
def main() -> None:
    """ Make a jazz noise here """

    args = get_args()

# --------------------------------------------------
if __name__ == '__main__':
    main()