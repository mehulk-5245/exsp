#suggest some better approach if possible
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name')
    return '<h1>Hello, ' + name + '!</h1>'

if __name__ == '__main__':
    app.run()
