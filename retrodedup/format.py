# -*- coding: utf-8 -*-
import logging
import re
import sys


class Format:
    NO_MATCH_ERROR = 20

    @classmethod
    def extract(cls, file):
        filename = file[0]
        filepath = file[1]
        regex = r"""
                ^(?P<title>.+){1}
                (?:\s)
                (?:\((?P<year>[0-9\-x]{4,10})\)){1}
                (?:\((?P<editor>[\w\.\-\s\!,&]+)\)){1}
                (?:\([0-9A-Z]+\))?
                (?:\((?P<disks>Disk\s[0-9]{1,}\sof\s[0-9]{1,})\))?
                (?:\([\w&\s]+\))*
                (?:\[cr\s(?P<crack>[\w\-&\s]+)?\])?
                (?:.*)
                $
                """

        match = re.match(regex, filename, re.MULTILINE | re.VERBOSE)
        if match is None:
            logging.error(f'No match for file {filename}')
            sys.exit(cls.NO_MATCH_ERROR)
        else:
            result = match.groupdict()
            result.update({'path': filepath})
            return result
