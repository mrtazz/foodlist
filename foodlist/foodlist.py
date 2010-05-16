"""
    groceries export
    module to produce Groceries.app importable output
"""

import json
import sys
from urllib import quote


class FoodList:
    """ Exporting a YAML groceries list as an import
        for Groceries.app
    """
    def __init__(self, aisles_json_file):
        try:
            aisles_json = json.loads(open(aisles_json_file).read())
        except IOError:
            sys.exit(-1)
        self.data = None
        # the aisles as imported from the json dump
        self.aisles_raw = aisles_json["aisles"]
        # the aisles for matching the list items against
        self.aisles_master = {}
        # the list data which in different format
        self.list_data = []
        for aisle in self.aisles_raw:
            self.aisles_master[aisle["name"]] = {"id" : aisle["id"],
                                                 "image" : aisle["imageName"]}

    def set_groceries(self, groceries):
        """ set groceries list """
        self.groceries = groceries

    def export_list(self, groceries, name = "Imported Groceries"):
        """ export groceries to correct format and
            returns it as string
        """
        if not self.data:
            self.build_groceries_data(groceries, name)
        return quote(json.dumps(self.data))

    def build_groceries_data(self, groceries, name = "Imported Groceries"):
        """ build the complete groceries data set """
        data = {}
        grocs = self.convert_groceries(groceries)
        data["items"] = grocs
        data["name"] = name
        data["aisles"] = self.aisles_raw
        self.data = data

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
                # build data for groceries export
                new_item = {}
                if aisle:
                    new_item["aisle"] = aisle["id"]
                new_item["name"] = item
                # build data for internal usage
                new_list_item = {}
                if aisle:
                    new_list_item["aisle"] = {"aislename":aisles,
                                              "aislecat": aisle["imageName"]}
                new_list_item["name"] = item
                self.list_data.append(new_list_item)

                ret.append(new_item)

        return ret
