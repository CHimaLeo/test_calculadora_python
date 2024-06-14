import http.client
import os
import unittest
from urllib.error import HTTPError
from urllib.request import urlopen

import pytest

BASE_URL = "http://127.0.0.1:5000"
DEFAULT_TIMEOUT = 2  # in secs


#@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add_ok(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_add_no_ok(self):
        url = f"{BASE_URL}/calc/add/'2'/2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    
    def test_api_substract_ok(self):
        url = f"{BASE_URL}/calc/substract/2/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_substract_no_ok(self):
        url = f"{BASE_URL}/calc/substract/'2'/2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
        
    def test_api_multiply_ok(self):
        url = f"{BASE_URL}/calc/multiply/2/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_multiply_no_ok(self):
        url = f"{BASE_URL}/calc/multiply/'2'/2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    
    def test_api_divide_ok(self):
        url = f"{BASE_URL}/calc/divide/2/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_divide_no_ok(self):
        url = f"{BASE_URL}/calc/divide/'2'/2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
        
    def test_api_divide_no_ok_cero(self):
        url = f"{BASE_URL}/calc/divide/2/0"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    
    def test_api_power_ok(self):
        url = f"{BASE_URL}/calc/power/2/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_power_no_ok(self):
        url = f"{BASE_URL}/calc/power/'2'/2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    
    def test_api_sqrt_ok(self):
        url = f"{BASE_URL}/calc/sqrt/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_sqrt_no_ok(self):
        url = f"{BASE_URL}/calc/sqrt/'2'"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
        
    def test_api_sqrt_no_ok_negativo(self):
        url = f"{BASE_URL}/calc/sqrt/-2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    
    def test_api_log10_ok(self):
        url = f"{BASE_URL}/calc/log10/2"
        response = urlopen(url)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )
    
    def test_api_log10_no_ok(self):
        url = f"{BASE_URL}/calc/log10/'2'"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
        
    def test_api_log10_no_ok_cero(self):
        url = f"{BASE_URL}/calc/log10/0"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    
    def test_api_log10_no_ok_negativo(self):
        url = f"{BASE_URL}/calc/log10/-2"
        with self.assertRaises(HTTPError) as cm:
            response = urlopen(url)
        
        self.assertEqual(cm.exception.code, 400)
    