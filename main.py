#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from pathlib import Path
from pprint import pprint

from retrodedup.format import Format
from retrodedup.romlist import RomList


def parseargs():
    parser = argparse.ArgumentParser(
        description='Deduplicate Romset from TOSEC (originaly build for Amiga ROMS)'
    )

    parser.add_argument('romset_dir', help='Romset directory')

    parser.add_argument('-r', '--recursive', help='scan romset recursively', action='store_true')
    parser.add_argument('-c', '--crack', help='try to keep files from this cracker')
    parser.add_argument('-e', '--extension', help='file extension for romfile', default='adf')
    parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')

    args = parser.parse_args()

    if not Path(args.romset_dir).resolve().is_dir():
        logging.error('%s is not a valid directory', args.romset_dir)
        sys.exit(1)

    return args


def main():
    roms = []

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.DEBUG)
    handler.addFilter(lambda record: record.levelno <= logging.INFO)
    verb_handler = logging.StreamHandler(sys.stderr)
    verb_handler.setLevel(logging.WARNING)
    logging.basicConfig(format='%(levelname)s:%(message)s', handlers=[handler, verb_handler])

    args = parseargs()

    logging.getLogger().setLevel(logging.INFO if args.verbose else logging.WARNING)

    romset = RomList(args.romset_dir)
    romfiles = romset.scandir(args.extension)
    romfiles.sort(key=lambda k: k[0])

    for rom in romfiles:
        roms.append(Format.extract(rom))

    pprint(roms[2628])  # Dragon's Breath Disk 1


if __name__ == '__main__':
    main()
