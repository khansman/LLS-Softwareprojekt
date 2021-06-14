import sys

from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_socketio import SocketIO
import arp_sender
import arp_receiver
import threading
import eventlet
eventlet.monkey_patch()

clients = 'test'

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.config['SECRET_KEY'] = '#45!54#mY_sEcrEt_KeY#45!54#'
socketio = SocketIO(app, logger=True, engineio_logger=True, async_mode='eventlet')
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    socketio.emit('connect_response', {'data': 'Connected!'})
    print('SID= '+request.sid)
    global clients
    clients = request.sid
    print('GLOBAL = '+clients)


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected!')


@socketio.on('json')
def handle_jsonIncome(json):
    print("Received JSON: " + str(json))
    arp_sender.call_sender(json['ip'], '10', json['message'])
    sendJson("Nachricht erfolgreich empfangen!")


@socketio.on('message')
def handle_MessageIncome(msg):
    print("Receive Message: " + msg)


def sendJson(message: str):
    print('SID_SendJSON '+clients)
    socketio.emit('json', {'data': message}, room=clients)

# @app.route('/send', methods=['POST'])
# def send():
#    val = request.json
#    jsonList.append(val)
#    print(val)
#    print(jsonList)
#    return render_template('index.html')


# @app.route('/receive', methods=['GET'])
# def receive():
#    val = "result"
#    return jsonify()


def start_websocket():
    try:
        socketio.run(app)
    except KeyboardInterrupt:
        arpReceiver_thread.join()
        sys.exit(0)




if __name__ == '__main__':
    #socketio.start_background_task(target=arp_receiver.call_receiver, app=app)
    arpReceiver_thread = threading.Thread(target=arp_receiver.call_receiver)
    arpReceiver_thread.daemon = True
    arpReceiver_thread.start()
    #arpReceiver_thread = multiprocessing.Process(target=arp_receiver.call_receiver)
    #arpReceiver_thread.start()
    start_websocket()

