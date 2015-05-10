from flask import Flask
from flask import make_response
from flask import jsonify
from flask import redirect

from werkzeug import exceptions

from functools import wraps

import arrow

import signs
import divination


def json_endpoint(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        response = f(*args, **kwargs)
        return make_response(jsonify({'data': response}))
    return decorated


def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return redirect("https://github.com/jimmytheleaf/astrologly")
  
    @app.route('/natal/<int:year>/<int:month>/<int:day>/<int:hour>/<int:minute>/')
    @json_endpoint
    def reading(year, month, day, hour, minute):

        date = arrow.get(year, month, day, hour, minute)
        response = divination.get_full_reading(date)
        return response

    @app.route('/natal/<int:year>/<int:month>/<int:day>/')
    @json_endpoint
    def day_reading(year, month, day):

        date = arrow.get(year, month, day)
        response = divination.get_base_reading(date)

        return response

    @app.route('/signs/')
    @json_endpoint
    def list_signs():

        response = []
        for sign in signs.sign_list:
            response.append(sign._asdict())

        return response

    @app.route('/signs/<string:name>/')
    @json_endpoint
    def get_sign(name):

        sign = signs.sign_map.get(name.lower(), None)

        if sign is None:
            raise exceptions.NotFound("No sign named: %s" % name)

        return sign._asdict()

    @app.errorhandler(ValueError)
    def value_error(error):
        return make_response(jsonify({'error': str(error)}), 400)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    @app.errorhandler(Exception)
    def value_error(error):
        return make_response(jsonify({'error': str(error)}), 500)

    return app