# foodlist.py

## What can it do for you?
You use [Groceries.app](http://www.sophiestication.com/groceries/) on your iPhone?
You would rather compose your shopping list on your computer?
foodlist.py makes groceries.app compatible, importable lists.
The script needs a json dump of example groceries data (as the one in the data
folder)
to match aisles. It also needs a [mustache](http://mustache.github.com)
template for printing an HTML list to stdout. The HTML output can then be
mailed to your iphone or put on a webserver. If you click on the link on your
iPhone the list is imported into Groceries.app.

## Dependencies
The lib only uses python modules, but for the executable pyyaml and pystache
are needed:

    pip install pyyaml
    pip install pystache

## Usage
Create a yaml list like this:

    aisle:
    - food
    - more food
    produce
    - tomatoes
    - spinache

You can put your files in the default search lcoation or specify them as
options:

    ~/.foodlist/groceries.json
    ~/.foodlist/groceries.mustache

Then run:

    foodlist.py -j path/to/dump.json -t path/to/template.mustache groceries.yaml

or:

    foodlist.py groceries.yaml > groceries.html

## TODO
* interactive mode for matching aisles
* more (or any for that matter) test cases and error handling
* better packaging

## Thanks
[Sophia Teutschler](http://www.sophiestication.com/) for Groceries.app.
