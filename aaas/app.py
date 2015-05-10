from flask import Flask
from flask import make_response
from flask import jsonify

from werkzeug import exceptions

from functools import wraps
import arrow
import signs


def json_endpoint(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        response = f(*args, **kwargs)
        return make_response(jsonify({'data': response}))
    return decorated


def get_app():

    app = Flask(__name__)

    @app.route('/natal/<int:year>/<int:month>/<int:day>/')
    @json_endpoint
    def reading(year, month, day):

        response = {}
        response['source'] = {}

        date = {
            'year': year,
            'month': month,
            'day': day
        }

        response['source']['date'] = date
        arrowed = arrow.get(year, month, day)
        response['source']['humanized'] = arrowed.humanize()
        response['source']['verbose']  = arrowed.format('dddd MMMM D, YYYY')

        sun_sign = signs.get_sign(month, day)

        if sun_sign is None:
            raise Exception("Problem retrieving sign for %s, %s" % month, day)

        response['signs'] = {}

        response['signs']['sun'] = sun_sign._asdict()

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

    @app.errorhandler(Exception)
    def value_error(error):
        return make_response(jsonify({'error': str(error)}), 500)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    return app