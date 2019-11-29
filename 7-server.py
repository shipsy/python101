from flask import request, Response, Flask
import json
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Hello World'

@app.route('/uptime', methods=['GET'])
def index2():
    return Response(json.dumps({"success": True, "status": "Server is Up"}), status=200, mimetype='application/json')


validApiKeys = ['123']
def authentication_check(headers):
	if 'Api-Key' not in list(headers.keys()) and 'api-key' not in list(headers.keys()):
		return {"success": False, "reason": "API KEY NOT FOUND"}
	if headers['Api-Key'] in validApiKeys or headers['api-key'] in validApiKeys:
		return {"success": True}
	else:
		return {"success": False, "reason": "API KEY INVALID"}


@app.route('/main', methods=['GET', 'POST'])
def index3():
	if request.method == 'GET':
		return Response(json.dumps({"success": True, "status": "Server Running"}), status=200, mimetype='application/json')
	auth = authentication_check(request.headers)
	if not auth:
		return Response(json.dumps({"success": False, "reason": "Auth Failed"}), status=401, mimetype='application/json')
	return Response(json.dumps({"success": True, "status": "OK"}), status=200, mimetype='application/json')

if __name__ == "__main__":
	default_port = 5000
	app.run(threaded=True, host='0.0.0.0', port=default_port)


app.run(threaded=True, host='0.0.0.0', port=5000)
