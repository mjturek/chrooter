#! /usr/bin/env python

import argparse
import sys
from subprocess import call

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    cmd = args.cmd[0]
    handle_cmd(cmd)

def handle_cmd(cmd):
    out = call(["ldd", cmd])
    print out

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', type=str, nargs=1)
    parser.add_argument('new_root', type=str, nargs=1)
    return parser

if __name__=="__main__":
    main(sys.argv[1:])
