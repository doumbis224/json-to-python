#!/usr/bin/python3
# coding:utf-8

from json2python import Parser

import argparse
import os


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-i', '--input-file', help="json file"
    )
    parser.add_argument(
        '-o', '--output-file', help="python file generated"
    )

    args = parser.parse_args()

    if args.input_file is None or args.output_file is None:
        return -1

    if not os.path.exists(args.input_file):
        return -1

    j2p = Parser.from_json(args.input_file)
    j2p.to_python_file(args.output_file)

    return 0


if __name__ == '__main__':
    exit(main())
