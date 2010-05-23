#!/usr/bin/env python
# encoding: utf-8
"""
    executable to convert yaml input into groceries.app
    compatible shopping lists
"""

import sys
import foodlist as fl

from os.path import expanduser
from optparse import OptionParser

try:
    import yaml
except ImportError:
    print "Yaml module not available."
    sys.exit(-1)

try:
    import pystache
except ImportError:
    pystache = None

GROCERIES_PATH = expanduser("~")+"/.foodlist/groceries.json"
GROCERIES_TEMPLATE = expanduser("~")+"/.foodlist/groceries.mustache"


def init_parser():
    """method to init options parser"""
        # initialize parser
    usage = "usage: %prog [-b base_data_dump] [-t template] [-n name] [-f \
format] groceries.yaml"

    parser = OptionParser(usage, version="%prog "+fl.__version__)
    parser.add_option("-b", "--base-data", action="store",
                      dest="base_data", help="base data dump file")
    parser.add_option("-t", "--template", action="store", dest="template",
                      help="mustache template to fill")
    parser.add_option("-n", "--name", action="store", dest="name",
                      help="name of the list")
    parser.add_option("-f", "--format", action="store", dest="format",
                      help="output format")

    return parser.parse_args()

def main():
    """ main function
    """
    (options, args) = init_parser()

    if not options.base_data:
        base_data = GROCERIES_PATH
    else:
        base_data = options.groceries_json

    try:
        if not options.template:
            template = open(GROCERIES_TEMPLATE).read()
        else:
            template = open(options.template).read()

    except IOError:
        template = None

    try:
        groceries = yaml.safe_load(open(args[0]).read())
    except:
        print "No valid list data given."
        sys.exit(-1)

    if not options.name:
        ctx = fl.export_list(groceries, json_data=base_data)
    else:
        ctx = fl.export_list(groceries, options.name, json_data=base_data)

    if pystache is not None and template is not None:
        print pystache.render(template, ctx)
    else:
        print ctx


if __name__ == '__main__':
    main()
