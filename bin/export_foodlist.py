#!/usr/bin/env python
# encoding: utf-8
"""
    executable to convert yaml input into groceries.app
    compatible shopping lists
"""

import yaml
import sys
import pystache

from os.path import expanduser
from optparse import OptionParser
import foodlist as fl

GROCERIES_PATH = expanduser("~")+"/.foodlist/groceries.json"
GROCERIES_TEMPLATE = expanduser("~")+"/.foodlist/groceries.mustache"


def init_parser():
    """method to init options parser"""
        # initialize parser
    usage = "usage: %prog [-j groceries_dump] [-t template] groceries.yaml"
    parser = OptionParser(usage, version="%prog "+fl.__version__)
    parser.add_option("-j", "--groceries_dump", action="store",
                      dest="groceries_json", help="groceries json dump")
    parser.add_option("-t", "--template", action="store", dest="template",
                      help="mustache template to fill")
    parser.add_option("-n", "--name", action="store", dest="name",
                      help="name of the list")

    return parser.parse_args()

def main():
    """ main function
    """
    (options, args) = init_parser()

    if not options.groceries_json:
        groceries_file = GROCERIES_PATH
    else:
        groceries_file = options.groceries_json

    if not options.template:
        template = open(GROCERIES_TEMPLATE).read()
    else:
        template = open(options.template).read()

    groc = fl.FoodList(groceries_file)
    if groc == None:
        sys.exit(-1)
    groceries = yaml.safe_load(open(args[0]).read())
    if not options.name:
        (list_data, data_json) = groc.export_list(groceries)
    else:
        (list_data, data_json) = groc.export_list(groceries, options.name)

    ctx = {}
    ctx['groceries'] = data_json
    ctx['listname'] = groc.data['name']
    ctx['itemcount'] = len(groc.data['items'])
    ctx["items"] = list_data
    output = pystache.render(template, ctx)
    print output


if __name__ == '__main__':
    main()
