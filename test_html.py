import os
import unittest

class TestHTML(unittest.TestCase):

    def test_html_exists(self):
        self.assertTrue(os.path.exists("index.html"), "El archivo index.html no existe")

    def test_html_content(self):
        with open("index.html", "r", encoding="utf-8") as f:
            contenido = f.read()
            self.assertIn("Hola Mundo", contenido, "El archivo no contiene 'Hola Mundo'")

if __name__ == "__main__":
    unittest.main()
