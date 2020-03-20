import json
import os
from functools import wraps
from werkzeug.exceptions import ServiceUnavailable, NotFound

import requests
from flask import Flask, jsonify
from typing import Dict

from config import ROOT_PATH

app = Flask(__name__)

with open(os.path.join(ROOT_PATH, 'data\\users.json'), 'r') as f:
    users = json.load(f)


def is_user_valid(fn):
    """
    This decorator is use to validate user against users.json database

    wraps - internally invokes update_wrapper method which update the wrapper_fn function to look like wrapped function
    (fn example users_by_id) which avoids "View function mapping overwrite error" occurs when you try to wrap more than
    one function with 2 or more decorator function
    Another way to overcome this error is to use 'endpoint' parameter in app.route method
    """
    @wraps(fn)
    def wrapper_fn(user_id):
        print("inside decorator function")
        if user_id not in users:
            print('user not valid')
            return jsonify({'Failure': 'Invalid user'})
        return fn(user_id)
    return wrapper_fn


@app.route('/')
def index():
    return jsonify({'index': 'users page'})


@app.route('/users', methods=['GET'])
def fetch_all_users():
    return json.dumps(users, indent=4)


@app.route('/users/<user_id>', methods=['GET'])  # endpoint='users_by_id' parameter
@is_user_valid
def users_by_id(user_id):
    return json.dumps(users.get(user_id), indent=4)


@app.route('/users/<user_id>/bookings', methods=['GET'])
@is_user_valid
def user_bookings(user_id) -> Dict:
    """
    This endpoint request the bookings microservices to fetch bookings done by pass user
    and further requests movies microservices to fetch movie details
    :param user_id:
    :return: Dict user bookings
    """
    try:
        bookings_resp = requests.get('http://127.0.0.1:5001/bookings/{user}'.format(user=user_id))
    except requests.exceptions.ConnectionError:
        raise ServiceUnavailable('Bookings service is not available')

    if bookings_resp.status_code == 404:
        raise NotFound('No bookings found for this user')

    bookings_data = bookings_resp.json()
    show_result = {}
    for date, movies in bookings_data.items():
        show_result[date] = []
        for movie_id in movies:
            try:
                movies_resp = requests.get('http://127.0.0.1:5002/movies/{movie}'.format(movie=movie_id))
            except requests.exceptions.ConnectionError:
                raise ServiceUnavailable('Movies service is not available')

            movie_data = movies_resp.json()
            show_result[date].append({
                "title": movie_data["title"],
                "rating": movie_data["rating"],
                "director": movie_data["director"]
            })

    return json.dumps(show_result, indent=4)


if __name__ == '__main__':
    app.run(port=5003, debug=True)
