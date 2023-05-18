# app is an instance of Flask created in __init__.py in directory codeflask
# codeflask is set as a python directory via __init__.py file.
from codeflask import app

if __name__ == "__main__":
    app.run(debug=True)


