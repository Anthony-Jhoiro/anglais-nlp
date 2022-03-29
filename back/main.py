from time import sleep
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS





app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

CORS(app, resources={"*": {"origins": "*"}})


@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

    sleep(3)

    emit("mess", "1234")




if __name__ == '__main__':
    socketio.run(app)