"""
    groceries export
    module to produce Groceries.app importable output
"""

import json


class GroceriesExporter:
    """ Exporting a YAML groceries list as an import
        for Groceries.app
    """
    def __init__(self, aisles_json_file):
        aisles_json = json.loads(open(aisles_json_file).read())
        self.aisles_raw = aisles_json["aisles"]
        self.aisles = {}
        for aisle in aisles_raw:
            aisles[aisle["name"]] = aisle["id"]

    def set_groceries(self, groceries):
        """ set groceries list """
        self.groceries = groceries

    def export_list(self, groceries, filepath):
        """ export groceries to given file """
        return

    def convert_groceries(self, groceries_list):
        """ converts a groceries yaml list into the
            format needed by groceries.app
        """
        ret = {}
        for aisles in groceries_list.keys():
            for items in groceries_list[aisles]:
                try:


        return ret
