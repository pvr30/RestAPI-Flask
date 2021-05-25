from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"vishal":{"age":20, "gender":"male"},
         "harsh":{"age":21, "gender":"male"}}

class HelloWorld(Resource):
    def get(self):
        return {'data': 'Hello World'}
    
    # Passing Arguments
    def get(self, name, age):
        return {"name": name,  "age": age}

    def post(self):
        return {'data': 'Post Request'}

    def get(self,name):
        return names[name]

#api.add_resource(HelloWorld, '/helloworld/<string:name>/<int:age>')
api.add_resource(HelloWorld, '/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)