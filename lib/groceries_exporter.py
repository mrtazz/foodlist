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
        try:
            aisles_json = json.loads(open(aisles_json_file).read())
        except IOError:
            return -1
        self.aisles_raw = aisles_json["aisles"]
        self.aisles_master = {}
        for aisle in aisles_raw:
            aisles_master[aisle["name"]] = aisle["id"]

    def set_groceries(self, groceries):
        """ set groceries list """
        self.groceries = groceries

    def export_list(self, groceries, filepath):
        """ export groceries to given file """
        return

    def convert_groceries(self, groceries_list):
        """ converts a groceries list into the
            format needed by groceries.app

            Params: groceries_list
            Format: {'aisle1': ['item1', 'item2'],
                     'aisle2': ['item3', 'item4']}

            Return:
                array of groceries in correct format
        """
        ret = []
        for aisles in groceries_list.keys():
            for item in groceries_list[aisles]:
                try:
                    aisle = self.aisles_master[aisles]
                except KeyError:
                    aisle = None
                new_item = {}
                if aisle:
                    new_item["aisle"] = aisle
                new_item["name"] = items
                ret.append(new_item)

        return ret
