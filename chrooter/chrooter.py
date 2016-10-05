#! /usr/bin/env python

import argparse
import os
import shutil
import sys
from command import Command
from environment import Environment

def main(argv):
    parser = build_parser()
    args = parser.parse_args(argv)
    cmd = args.cmd[0]
    new_root = args.new_root[0]
    handle_cmd(cmd, new_root)

def handle_cmd(cmd, new_root):
    command = Command(cmd)
    environment = Environment(new_root)
    environment.add_command(command)

def build_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', type=str, nargs=1)
    parser.add_argument('new_root', type=str, nargs=1)
    return parser

if __name__=="__main__":
    main(sys.argv[1:])
