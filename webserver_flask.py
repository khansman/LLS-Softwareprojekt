from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)
jsonList = []


@app.route('/', methods=['GET'])
def index():
    #val = "result"
    #return jsonify({"Jule": val})
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    val = request.json
    jsonList.append(val)
    print(val)
    print(jsonList)
    return render_template('index.html')


@app.route('/receive', methods=['GET'])
def receive():
    val = "result"
    return jsonify()


if __name__ == '__main__':
    app.run(debug=True)
