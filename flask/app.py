from flask import Flask

app = Flask(__name__)

@app.route('/hello-cse6242')
def index():
    return 'Hello from CSE6242 app!'


@app.route('/hello-backend')
def index():
    return 'Hello from backend app!'

app.run(host='0.0.0.0', port=81)