from flask import Flask

# a member of the app package - In Python, a sub-directory that includes a __init__.py file is considered a package,
# and can be imported.
# The __name__ variable passed to the Flask class is a Python predefined variable,
# which is set to the name of the module? (package also)? in which it is used.
microblogApp = Flask(__name__)
print("__name__: " + str(__name__))

# app here is the package which defined by this __init__.py
# routes is a module
# it reads from package import module
# importing routes module at the bottom cos routes will need to import application variable above
# The bottom import is a workaround to circular imports, a common problem with Flask applications.
from app import routes
