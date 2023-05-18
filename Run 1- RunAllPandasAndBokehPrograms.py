import os               # needed for directory and file listing
import re               # import regular expressions module for string search
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

datapath = './'  # project's root directory where all the packages are installed
substring = "ipynb"

with os.scandir(datapath) as entries:
    for entry in entries:
        if entry.is_file() and re.search(substring, entry.name):
            print('Executing: ', entry.name, '\n')
            # """"
            with open(entry.name) as ff:  # Reference: https://nbconvert.readthedocs.io/en/latest/execute_api.html
                nb_in = nbformat.read(ff, nbformat.NO_CONVERT)
            ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
            nb_out = ep.preprocess(nb_in)  
            # """
print('All Pandas and Bokeh programs executed!', '\n')


# end of file

