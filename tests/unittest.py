import os
import unittest
import requests
  
class ApiTest(unittest.TestCase):
    API_URL = "http://127.0.0.1:1234/api"
    GOOGLE_URL = "{}/google_activity".format(API_URL)

    def test_get_all_activity(self):
        r = requests.get(ApiTest.GOOGLE_URL)
        self.assertEqual(r.status_code,200)
        self.assertNotEqual(len(r.json()),0)

if __name__ == "__main__":
    unittest.main()