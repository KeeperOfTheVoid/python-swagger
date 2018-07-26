from flask import Flask

# Asks app to import Flask.  Flask is used to create instances of Web Applications
# __name__ is a special var in Python.  __main__ can be used if it's being executed
# as main program
app = Flask(__name__)

# Decorator defines route
@app.route("/hello")
def hello():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)