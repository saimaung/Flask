# from package import member
from app import microblogApp
from flask import render_template

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
    user = {'username': 'Sai Wai Maung'}
    # To represent user posts I'm using a list, where each element is a dictionary that has author and body fields.
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Monsoon season in Yangon!'
        },
        {
            'author': {'username': 'Chen'},
            'body': 'Raptors takes game 3!'
        }
    ]
    # <!---
    # The only interesting thing in index.html page is that there are a couple of placeholders for the dynamic content,
    # enclosed in {{ ... }} sections.
    # These placeholders represent the parts of the page that are variable and will only be known at runtime.
    # -->
    return render_template('index.html', title='Sai', user=user, posts=posts)
