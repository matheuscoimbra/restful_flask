"""
Casos de Teste

execução: python reclame_pytest.py

"""

import unittest
import requests
import json

class ReclamacaoTestCase(unittest.TestCase):

    # def setUp(self):
    #     self.app = app.test_client()

    def test_create_complain(self):
        """Test API (POST request)."""
        dat = {"titulo": "produto nao chegou10",
               "descricao": "notebook ainda não edffd chegou",
               "local": "são luis",
               "companhia": "Apple"}
        json_string = json.dumps(dat)
        headers = {'content-type': 'application/json'}
        print(json_string)
        response = requests.post('http://localhost:5000/reclamacao', headers=headers, data=json_string)
        self.assertEqual(response.status_code, 200)

    def test_put_complain(self):
        """Test API (PUT request)."""
        dat = {"titulo": "produto nao chegou10",
               "descricao": "notebook ainda não edffde chegou",
               "local": "são luis",
               "companhia": "Apple"}
        json_string = json.dumps(dat)
        headers = {'content-type': 'application/json'}
        print(json_string)
        response = requests.put('http://localhost:5000/reclamacao/5b6b5c123a05e650a48908dc', headers=headers, data=json_string)
        self.assertEqual(response.status_code, 200)

    def test_del_complain(self):
        """Test API (DELETE request)."""
        response = requests.delete('http://localhost:5000/reclamacao/5b6b5c123a05e650a48908dc')
        self.assertEqual(response.status_code, 200)

    def test_get_all_complain(self):
        """Test API (GET request)."""
        response = requests.get('http://localhost:5000/reclamacao')
        self.assertEqual(response.status_code, 200)

    def test_get_single_complain(self):
        """Test API (GET request)."""
        response = requests.get('http://localhost:5000/reclamacao/5b6b450a3a05e6570cfe8959')
        self.assertEqual(response.status_code, 200)

    def test_get_most_company_complain(self):
        """Test API (GET request)."""
        response = requests.get('http://localhost:5000/reclamacao/maior/companhia')
        self.assertEqual(response.status_code, 200)

    def test_get_less_company_complain(self):
        """Test API (GET request)."""
        response = requests.get('http://localhost:5000/reclamacao/menos/companhia')
        self.assertEqual(response.status_code, 200)

    def test_get_most_locale_complain(self):
        """Test API (GET request)."""
        response = requests.get('http://localhost:5000/reclamacao/maior/local')
        self.assertEqual(response.status_code, 200)

    def test_get_less_locale_complain(self):
        """Test API (GET request)."""
        response = requests.get('http://localhost:5000/reclamacao/menos/local')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()