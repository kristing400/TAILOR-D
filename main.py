from flask.ext.api import FlaskAPI
app = FlaskAPI(__name__)



@app.route('/', methods=['GET'])
def test():
	return {'hello': 'world'}
