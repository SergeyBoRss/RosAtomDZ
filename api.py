import flask
import os

app = flask.Flask(__name__)
app.config['DEBUG'] = True

port= int(os.environ.get('PORT', 5000))

@app.route('/', methods=['GET'])
def index():
    return '<h1>INDEX</h1>'

app.run(
    host='0.0.0.0',
    port=port
)
