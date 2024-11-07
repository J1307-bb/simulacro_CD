# tests/test_app.py
import unittest
from app import saludo

class TestApp(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo(), "Hola, Mundo")

if __name__ == "__main__":
    unittest.main()
