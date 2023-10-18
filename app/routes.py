from flask import Flask # from the flask module impott the Flask class

# OOP -> Obejct Oriented Paradigm (class is to an object what a blue print is to an house)
app = Flask(__name__)         # create an instance of Flask (an object)
                            # Variables that belong to a class
                            # are called (class) attributes.
                            # fucntions that belong to a class
                            # are called "methods"
@app.get("/")               # Flask decorator
def index():                # View Function
    me = {                  # Python dictionary
        "first_name": "Mark",
        "last_name": "McKie",
        "hobbies": "Passive Income",
        "is_active": True
    }
    return me               # return statement (JSON)

    # A decorator is simply a function
    # that "wraps" another function
    # Means that the wrapping funciton takes
    # a funcitn as a parameter
    # high level example:
    # def wrapper_fucntion(other_func):
    #     # do stuff here
    #     value = other_func()
    #     # do stuff here
    #     return value