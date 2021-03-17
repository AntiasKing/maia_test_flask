from flask import Flask, jsonify, request
from flask_cors import CORS

from notification import Notification

app = Flask(__name__)
CORS(app)

notifs = []

@app.route('/')
def index():
  return 'It works'

@app.route('/notifications', methods=['GET'])
def notifications():
  print(notifs)
  data = []
  for n in notifs:
    data.append(n.toJSON())
  return jsonify(data), 200

@app.route('/notification', methods=['POST'])
def create_notification():
  if request.is_json:
    data = request.get_json()
    n = Notification(len(notifs), data['msg'])
    notifs.append(n)
    return 'Notification created', 201
  else:
    print(request)
    return 'Bad Request', 400

@app.route('/notification/<id>', methods=['GET', 'PUT'])
def notification(id=None):
  try:
    id = int(id)
    if request.method == 'GET':
      return notifs[int(id)], 200
    elif request.method == 'PUT':
      notifs[int(id)].toggleRead()
      return jsonify(notifs[id].toJSON()), 200
  except:
    return 'Bad Request', 400
