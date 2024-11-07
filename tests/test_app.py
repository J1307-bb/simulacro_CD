
import unittest
from app import saludo
from app import despedida

class TestApp(unittest.TestCase):
    def test_saludo(self):
        self.assertEqual(saludo(), "Hola, Mundo")
    def test_despedida(self):
        self.assertEqual(despedida(), "Adiós, Mundo")

if __name__ == "__main__":
    unittest.main()
