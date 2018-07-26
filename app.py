from flask import Flask
from flask_restplus import Resource, Api

# Asks app to import Flask.  Flask is used to create instances of Web Applications
# __name__ is a special var in Python.  __main__ can be used if it's being executed
# as main program

app = Flask(__name__)
api = Api(app, version='1.0', title='Sample API',
    description='A Sample API')

# Decorator defines route
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)