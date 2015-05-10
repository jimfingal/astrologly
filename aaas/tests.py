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
        signs = json.loads(self.app.get("/signs/").data)
        self.assertEqual(len(signs['data']), 12)