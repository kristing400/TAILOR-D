from flask.ext.api import FlaskAPI
app = FlaskAPI(__name__)



@app.route('/test')
def test():
	return {'hello': 'world'}
