import flask

app = flask.Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def index():
    return '<h1>INDEX</h1>'

app.run(
    host='127.0.0.1'
)