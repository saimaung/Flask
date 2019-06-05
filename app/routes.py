# from package import member
from app import microblogApp

# In Flask, handlers for the application routes are written as Python functions, called view functions.
# View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests
# a given URL.
# The two strange @app.route lines above the function are decorators, a unique feature of the Python language.
# A decorator modifies the function that follows it.
# A common pattern with decorators is to use them to register functions as callbacks for certain events.
# In this case, the @app.route decorator creates an association between the URL given as an argument and the function.
# In this example there are two decorators, which associate the URLs / and /index to this function.
# This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and
# pass the return value of it back to the browser as a response.


@microblogApp.route('/')
@microblogApp.route('/index')
def index():
    return "Hello World!"
