import argparse
parser = argparse.ArgumentParser(
    description='Shows you characteristics of 1st Gen. Pokemon')
subparser = parser.add_subparsers()
args = parser.parse_args()
parser.add_argument('list',)
subparser.add_parser()
