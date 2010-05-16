# groceries_exporter.py

## What?
Surprisingly it makes [Groceries.app](http://www.sophiestication.com/groceries/)
compatible, importable lists. The script needs a json dump of example groceries
data to match aisles. It also needs a [mustache](http://mustache.github.com)
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

Then run:

    groceries_exporter.py -j path/to/dump.json -t path/to/template.mustache groceries.yaml


## TODO
* interactive mode to choose aisles
* more test cases and error handling

## Thanks
Sophia Teutschler [Sophiestication Software](http://www.sophiestication.com/)
for Groceries.app
