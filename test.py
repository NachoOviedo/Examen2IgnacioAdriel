import unittest
from Examen2 import MiClase


class TestMiClase(unittest.TestCase):
    
    def setUp(self):
        """Configura una instancia de MiClase antes de cada prueba"""
        self.objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2"], [0.8, 0.9])
    
    # Pruebas para ObtieneValencia
    def test_ObtieneValencia_con_varios_impares(self):
        """Prueba con un número que tiene varios dígitos impares"""
        resultado = self.objeto.ObtieneValencia(1234567)
        self.assertEqual(resultado, 4)  # 1, 3, 5, 7 son impares
    
    def test_ObtieneValencia_solo_pares(self):
        """Prueba con un número que solo tiene dígitos pares"""
        resultado = self.objeto.ObtieneValencia(2468)
        self.assertEqual(resultado, 0)  # No hay dígitos impares
    
    # Pruebas para DivisibleTempo
    def test_DivisibleTempo_numero_pequeno(self):
        """Prueba con un número pequeño"""
        resultado = self.objeto.DivisibleTempo(10)
        self.assertEqual(resultado, [1, 2, 5, 10])
    
    def test_DivisibleTempo_numero_primo(self):
        """Prueba con un número primo"""
        resultado = self.objeto.DivisibleTempo(7)
        self.assertEqual(resultado, [1, 7])
    
    # Pruebas para ObtieneMasBailable
    def test_ObtieneMasBailable_lista_normal(self):
        """Prueba con una lista normal de valores"""
        resultado = self.objeto.ObtieneMasBailable([0.8, 0.9, 0.7])
        self.assertEqual(resultado, 0.9)
    
    def test_ObtieneMasBailable_lista_vacia(self):
        """Prueba con una lista vacía"""
        resultado = self.objeto.ObtieneMasBailable([])
        self.assertIsNone(resultado)
    
    # Pruebas para VerificaListaCanciones
    def test_VerificaListaCanciones_todas_validas(self):
        """Prueba con una lista donde todas las canciones son válidas"""
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"])
        self.assertTrue(resultado)
    
    def test_VerificaListaCanciones_con_none(self):
        """Prueba con una lista que contiene None"""
        resultado = self.objeto.VerificaListaCanciones(["Canción 1", None, "Canción 3"])
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
