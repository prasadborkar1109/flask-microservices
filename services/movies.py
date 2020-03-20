import json
import os

from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

from config import ROOT_PATH

app = Flask(__name__)

with open(os.path.join(ROOT_PATH, 'data\\movies.json'), 'r') as f:
    movies = json.load(f)


@app.errorhandler(404)
def page_not_found(error):
    raise NotFound


@app.route('/')
def index():
    return jsonify({'index': 'movies page'})


@app.route('/movies', methods=['GET'])
def fetch_all_movies():
    return json.dumps(movies, indent=4)


@app.route('/movies/<movie_id>', methods=['GET'])
def movie_by_id(movie_id):
    if movie_id not in movies:
        return jsonify({'Failure': 'No movie found for given id'})
    return json.dumps(movies.get(movie_id), indent=4)


if __name__ == '__main__':
    app.run(port=5002, debug=True)
