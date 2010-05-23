# encoding: utf-8
""" package init for meta data and method export """

from foodlist import FoodList

__author__ = "Daniel Schauenberg"
__version__ = "0.1.0"
__license__ = "MIT"

def export_list(groceries, **kwargs):
    """ export_list method export for easy access """
    return FoodList().export_list(groceries, **kwargs)
