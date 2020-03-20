import json
import os

from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

from config import ROOT_PATH

app = Flask(__name__)

with open(os.path.join(ROOT_PATH, 'data\\bookings.json'), 'r') as f:
    bookings = json.load(f)


@app.errorhandler(404)
def page_not_found(error):
    raise NotFound


@app.route('/')
def index():
    return jsonify({'index': 'bookings page'})


@app.route('/bookings', methods=['GET'])
def fetch_all_bookings():
    print('inside bookings')
    print(bookings)
    return json.dumps(bookings, indent=4)


@app.route('/bookings/<user>', methods=['GET'])
def bookings_by_user(user):
    if user not in bookings:
        return NotFound('No bookings found for this user')
    return json.dumps(bookings.get(user), indent=4)


if __name__=='__main__':
    app.run(port=5001, debug=True)
