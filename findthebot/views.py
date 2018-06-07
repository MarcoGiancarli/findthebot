from findthebot import app, socketio
from flask import render_template
from flask_socketio import send

@app.route('/')
def index():
    return render_template('test.html')

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)
