# encoding: utf-8
"""
    foodlist
    module to produce Groceries.app importable output
"""

import json
from urllib import quote

class FoodList:
    """ Exporting a YAML groceries list as an import
        for Groceries.app
    """
    def __init__(self):
        """ init the available list formats
        """
        self.listformats = {
                              "groceries.app" : self.convert_groceries_app
                           }

    def export_list(self, groceries, **kwargs):
        """ export groceries list

            Parameters:
                groceries -> the yaml parsed list
                name -> the name of the output list
                format_ -> the format for converting the list

            Returns:
                Context for requested format
        """
        format_ = kwargs["format"]
        return self.listformats.get(format_)(groceries, **kwargs)

# converter methods for different formats

    def convert_groceries_app(self, groceries_list, name, **kwargs):
        """ converts a groceries list into the
            format needed by groceries.app

            Params: groceries_list
            Format: {'aisle1': ['item1', 'item2'],
                     'aisle2': ['item3', 'item4']}

            Return:
                context for mustache template
        """


        # open and parse json file
        try:
            json_data = kwargs["base_data"]
        except KeyError:
            raise MissingParameterError("Path to json dump of groceries.app\
 base data not provided.")
        try:
            aisles_json = json.loads(open(json_data).read())
        except IOError:
            print json_data
            raise BaseDataError("No groceries.app json dump available.")

        # preparse groceries.app data for easy access later on
        # the aisles as imported from the json dump

        # the aisles for matching the list items against
        aisles_master = {}
        for aisle in aisles_json["aisles"]:
            aisles_master[aisle["name"]] = {"id" : aisle["id"],
                                            "image" : aisle["imageName"]}

        list_data = []
        groceries = []
        for aisles in groceries_list.keys():
            for item in groceries_list[aisles]:
                try:
                    aisle = aisles_master[aisles]
                except KeyError:
                    aisle = None
                # build data for groceries export
                new_item = {}
                if aisle is not None:
                    new_item["aisle"] = aisle["id"]
                new_item["name"] = item
                # build data for internal usage
                new_list_item = {}
                if aisle:
                    new_list_item["aisle"] = {"aislename":aisles,
                                              "aislecat": aisle["imageName"]}
                new_list_item["name"] = item
                # append item to arrays
                list_data.append(new_list_item)
                groceries.append(new_item)

        ctx = {}
        ctx['groceries'] = quote(json.dumps({"items" : groceries, 'name' : name,
                                             "aisles" : aisles_json['aisles']}))
        ctx['listname'] = name
        ctx['itemcount'] = len(groceries)
        ctx["items"] = list_data

        return ctx

# Exception classes
class BaseDataError(Exception):
    """ exception to raise if data needed for constructing a specific format
        is missing.
    """
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return repr(self.arg)

class MissingParameterError(Exception):
    """ exception to raise if not all needed parameters were provided to
        a converter method.
    """
    def __init__(self, arg):
        self.arg = arg
    def __str__(self):
        return repr(self.arg)

