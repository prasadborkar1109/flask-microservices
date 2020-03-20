import json
import os

from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

from config import ROOT_PATH

app = Flask(__name__)

with open(os.path.join(ROOT_PATH, 'data\\showtimes.json'), 'r') as f:
    showtimes = json.load(f)


# @app.errorhandler(404)
# def page_not_found(error):
#     raise NotFound


@app.route('/')
def index():
    return jsonify({'index': 'showtimes page'})


@app.route('/showtimes', methods=['GET'])
def fetch_all_shows():
    return json.dumps(showtimes, indent=4)


@app.route('/showtimes/<date>', methods=['GET'])
def movie_by_id(date):
    if date not in showtimes:
        return jsonify({'Failure': 'No movie shows available at provided date'})
    return json.dumps(showtimes.get(date), indent=4)


if __name__ == '__main__':
    app.run(port=5004, debug=True)
