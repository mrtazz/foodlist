foodlist.py
============

Export YAML shopping lists into different formats.

About:
-------

foodlist converts simple yaml shopping lists into different formats. This can
be done in order to get a better layout or make them importable for other
applications. Originally I built this to be able to write simple grocery lists
on my computer and import them into
Groceries.app_, a wonderful iPhone application for shopping lists.

I tried to built it as abstract as possible, so that new formats could be added
easily.

Dependencies:
--------------
pyyaml for input parsing and pystache for filling the output template. If
pystache is not available or no template was given, the context object is
simply printed onto the screen.

::

    pip install pyyaml
    pip install pystache

Installation:
-------------
The package itself can be installed via PyPi:

    pip install foodlist

Or if you must:

    easy_install foodlist

This does not install the example data from the data folder, however. They are
working examples, but I don't think they are useful enough to be bundled. If
you want to use or modify these examples, feel free to do this.

Usage:
-------
Create a yaml list like this:

::

    aisle:
    - food
    - more food
    produce:
    - tomatoes
    - spinache

The executable can be given optional paths for base data needed to convert the
list and a mustache template for output generation.

You can also put your files in the default search location:

::

    ~/.foodlist/groceries.json
    ~/.foodlist/groceries.mustache

Simple execution with groceries.app format and the default
base_data/template:

    export_foodlist.py list.yaml

Template and base data paths given explicitly:

    export_foodlist.py -b groceries.json -t groceries.mustache list.yaml

Additionally it is possible to pass a name and the format:

    export_foodlist.py -n "My awesome list" -f "groceries.app" list.yaml

Expansion:
----------
Adding new formats is rather easy. Just add a new converter method with the
signature:

    def new_converter_method(self, groceries_list, \*\*kwargs)

The parameters are:

* groceries_list = the object parsed from the yaml list
* \*\*kwargs additional arguments like base data path, etc

::

   kwargs = {
                "format" : "desired format",
                "name" : "name of the list",
                "base_data" : "path to base data file"
            }


Then add it to the listformats dict:

    listformats = {'keyword': self.new_converter_method}

And that's about it.

Caveats:
--------
Since I don't know if it is okay (license-wise) to bundle json data
from Groceries.app here, no data is included. However it is rather
easy to get a json dump yourself. Just export a shopping list from
Groceries.app and search in the plain email text for:

  groceries://import?from=YOURIPHONE&amp;data=

The part after data is the json data which needs to be fed to the application.

TODO:
------
* more (or any for that matter) test cases
* more formats

Thanks:
-------
Sophia Teutschler for Groceries.app.

.. _Groceries.app: http://www.sophiestication.com/groceries/
