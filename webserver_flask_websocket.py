import sys

import requests
from flask import Flask, render_template, request
from flask_cors import CORS
from flask_socketio import SocketIO
import arp_sender
import arp_receiver
import threading
import eventlet
import webbrowser

eventlet.monkey_patch()

app = Flask(__name__, static_folder='static', static_url_path='/static')
socketio = SocketIO(app, logger=True, engineio_logger=True, async_mode='eventlet')
CORS(app)

clients = ''
stop_flag = False


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/stop')
def shutdown_server():
    requests.post("http://127.0.0.1:5000", {"Connection":"close"})
    socketio.stop()
    return ''


@socketio.on('connect')
def handle_connect():
    socketio.emit('connect_response', {'data': 'Connected!'})
    print("Client connected: " + request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected: ' + request.sid)


@socketio.on('json')
def handle_jsonIncome(json):
    print("Received JSON: " + str(json))
    arp_sender.call_sender(json['ip'], '10', json['message'])
    #sendJson("Nachricht erfolgreich empfangen!")


@socketio.on('message')
def handle_MessageIncome(msg):
    print("Receive Message: " + msg)
    print('SID= ' + request.sid)
    global clients
    clients = request.sid
    print('GLOBAL = ' + clients)


@socketio.on('arp_receiver_message')
def handle_arp_connect(msg):
    message = msg["message"]
    sender_ip = msg["sender_ip"]
    message_to_client = "Nachricht von "+sender_ip+": "+message
    sendJson(message_to_client)


@socketio.on('shutdown')
def handle_shutdown_request():

    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(max_retries=20)
    session.mount('http://', adapter)
    session.get('http://127.0.0.1:5000/stop', headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"})
    arpReceiver_thread.join()


def sendJson(message: str):
    print('SID_SendJSON ' + clients)
    socketio.emit('json', {'data': message}, room=clients)


def start_websocket():
    try:
        socketio.run(app)
    except KeyboardInterrupt:
        arpReceiver_thread.join()
        sys.exit(0)


if __name__ == '__main__':
    arpReceiver_thread = threading.Thread(target=arp_receiver.call_receiver, args=())
    arpReceiver_thread.daemon = True
    arpReceiver_thread.start()
    website = webbrowser.open_new("http://127.0.0.1:5000")
    start_websocket()
