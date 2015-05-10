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

    def test_sign_index(self):
        index = signs.sign_index(signs.taurus)
        self.assertEqual(index, 1)

    def test_rising_diff(self):
        self.assertEquals(-2, signs.rising_diff(0, 30))
        self.assertEquals(0, signs.rising_diff(6, 00))
        self.assertEquals(6, signs.rising_diff(16, 01))
        self.assertEquals(-4, signs.rising_diff(21, 01))

    def test_rising_sign(self):

        self.assertEquals(signs.aquarius, signs.get_rising_sign(signs.aries, 1, 00))
        self.assertEquals(signs.pisces, signs.get_rising_sign(signs.aries, 3, 00))
        self.assertEquals(signs.aries, signs.get_rising_sign(signs.aries, 5, 00))
        self.assertEquals(signs.taurus, signs.get_rising_sign(signs.aries, 7, 00))
        self.assertEquals(signs.gemini, signs.get_rising_sign(signs.aries, 9, 00))
        self.assertEquals(signs.cancer, signs.get_rising_sign(signs.aries, 11, 00))
        self.assertEquals(signs.leo, signs.get_rising_sign(signs.aries, 13, 00))
        self.assertEquals(signs.virgo, signs.get_rising_sign(signs.aries, 15, 00))
        self.assertEquals(signs.libra, signs.get_rising_sign(signs.aries, 17, 00))
        self.assertEquals(signs.scorpio, signs.get_rising_sign(signs.aries, 19, 00))
        self.assertEquals(signs.sagittarius, signs.get_rising_sign(signs.aries, 21, 00))
        self.assertEquals(signs.capricorn, signs.get_rising_sign(signs.aries, 23, 00))


class APITest(unittest.TestCase):

    def setUp(self):

        self.app = app.create_app().test_client()

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

    def test_get_full_reading(self):
        response = self.app.get("/natal/1983/1/31/12/45/")
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)['data']

        self.assertIn('signs', data)
        self.assertIn('source', data)
        self.assertIn('sun', data['signs'])
        self.assertIn('rising', data['signs'])
        self.assertEqual('aquarius', data['signs']['sun']['name'].lower())
        self.assertEqual('gemini', data['signs']['rising']['name'].lower()) 