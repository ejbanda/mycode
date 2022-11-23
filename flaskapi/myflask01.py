#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
#    module       class

# variable "app" represents our entire api
# whole script is teaching our little app object how to behave
app = Flask(__name__) # __name__ == name of module we're currently running

#can put a data(variable) that the endpoints can pull from
#can import more modules
data = [
        {
            'backpack': ['chisel', 'bones'],
            'name': 'carl',
            'quest_points': 109
            },
        {
            'backpack': ['bandos godsword', 'saradomin brew'],
            'name': 'lisa',
            'quest_points': 0,
            'special': 75
            }

]



# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/eric") # decorator
def hello_world():
   return data

#this is another endpoint
@app.route("/json")
def json_example():
    return {'boolean': True, "value": None}

@app.route("/")
def hello_world():
   return "Hello World"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

