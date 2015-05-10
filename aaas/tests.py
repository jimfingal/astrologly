from flask import json

import unittest

import app
import signs


class SignTest(unittest.TestCase):

    def test_signs(self):

        self.assertEqual(len(signs.all_signs), 12)

    def test_sign_function(self):

        self.assertEqual(signs.get_sign(1, 31), signs.aquarius)
        self.assertEqual(signs.get_sign(3, 21), signs.aries)
        self.assertEqual(signs.get_sign(12, 25), signs.capricorn)
        self.assertEqual(signs.get_sign(1, 20), signs.capricorn)
        self.assertEqual(signs.get_sign(1, 21), signs.aquarius)


class APITest(unittest.TestCase):

    def setUp(self):

        self.app = app.get_app().test_client()

    def test_get_signs(self):
        response = self.app.get("/signs/?apikey=123")
        self.assertEqual(response.status_code, 200)

        signs = json.loads(response.data)
        self.assertEqual(len(signs['data']), 12)

    def test_get_sign(self):
        for sign in signs.sign_list:
            response = self.app.get("/signs/%s/" % sign.name.lower())
            self.assertEqual(response.status_code, 200)

    def test_get_sign_bad(self):
        response = self.app.get("/signs/foo/")
        self.assertEqual(response.status_code, 404)

    def test_get_reading(self):
        response = self.app.get("/natal/1983/1/31/")
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)['data']

        self.assertIn('signs', data)
        self.assertIn('source', data)
        self.assertIn('sun', data['signs'])
        self.assertEqual('aquarius', data['signs']['sun']['name'].lower())
