# __init__.py , among other things, labels a directory as a python directory and lets you
# set variables on a package wide level.
# __main__.py , among other things, is run if you try to run a compressed group of python files.
# __main__.py allows you to execute packages.
from flask import Flask

app=Flask(__name__)  # instantiate Flask object

from codeflask import routes  # all routes will be defined in this file





