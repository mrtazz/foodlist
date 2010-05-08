#!/usr/bin/env python
# encoding: utf-8
"""
    executable to convert yaml input into groceries.app
    compatible shopping lists
"""

import yaml
import sys

from os.path import expanduser
from optparse import OptionParser
from lib.__version__ import __version__
from lib.groceries_exporter import GroceriesExporter

GROCERIES_PATH = expanduser("~")+"/.groceries_exporter/groceries.json"
GROCERIES_TEMPLATE = expanduser("~")+"/.groceries_exporter/groceries.mustache"


def init_parser():
    """method to init options parser"""
        # initialize parser
    usage = "usage: %prog [-j groceries_dump] [-t template] groceries.yaml"
    parser = OptionParser(usage, version="%prog "+__version__)
    parser.add_option("-j", "--groceries_dump", action="store",
                      dest="groceries_json", help="groceries json dump")
    parser.add_option("-t", "--template", action="store", dest="template",
                      help="mustache template to fill")

    return parser.parse_args()

def main():
    """ main function
    """
    (options, args) = init_parser()

    if not options.groceries_json:
        groceries_file = GROCERIES_PATH
    else:
        groceries_file = options.groceries_json
    print groceries_file

    gc = GroceriesExporter(groceries_file)
    if gc == None:
        sys.exit(-1)
    groceries = yaml.safe_load(open(args[0]).read())
    print gc.export_list(groceries)

if __name__ == '__main__':
    main()
