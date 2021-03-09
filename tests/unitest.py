import os
import unittest
import requests
  
class ApiTest(unittest.TestCase):
    API_URL = "http://localhost:443/api/v1"
    
    ENDPOINT_ONE = "{}/activities".format(API_URL)
    ENDPOINT_TWO = "{}/activities/area_by_code/E09000001".format(API_URL)

    def test_get_all_activity(self):
        r = requests.get(ApiTest.ENDPOINT_ONE)
        self.assertEqual(r.status_code,200)
        self.assertNotEqual(len(r.json()),0)
    
    def test_area_by_code(self):
        r = requests.get(ApiTest.ENDPOINT_TWO)
        self.assertEqual(r.status_code,200)
        for i in r.json():
            self.assertEqual(i['area_name'],"City of London")

if __name__ == "__main__":
    unittest.main()