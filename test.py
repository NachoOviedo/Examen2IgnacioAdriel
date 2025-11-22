import unittest
from Examen2 import MiClase


class TestMiClase(unittest.TestCase):
    
    def setUp(self):
        """Configura una instancia de MiClase antes de cada prueba"""
        self.objeto = MiClase(7, 90, 8, ["Rock", "Pop", "Jazz"], [0.5, 0.6, 0.7])
    
    # ==================== Pruebas para ObtieneValencia ====================
    
    def test_ObtieneValencia_solo_impares(self):
        """Prueba con un número que solo tiene dígitos impares"""
        resultado = self.objeto.ObtieneValencia(13579)
        self.assertEqual(resultado, 5)  # Todos son impares: 1, 3, 5, 7, 9
    
    def test_ObtieneValencia_con_ceros(self):
        """Prueba con un número que contiene ceros"""
        resultado = self.objeto.ObtieneValencia(10203)
        self.assertEqual(resultado, 2)  # Solo 1 y 3 son impares
    
    # ==================== Pruebas para DivisibleTempo ====================
    
    def test_DivisibleTempo_numero_uno(self):
        """Prueba con el número 1"""
        resultado = self.objeto.DivisibleTempo(1)
        self.assertEqual(resultado, [1])
    
    def test_DivisibleTempo_numero_cuadrado_perfecto(self):
        """Prueba con un número cuadrado perfecto"""
        resultado = self.objeto.DivisibleTempo(16)
        self.assertEqual(resultado, [1, 2, 4, 8, 16])
    
    # ==================== Pruebas para ObtieneMasBailable ====================
    
    def test_ObtieneMasBailable_un_solo_elemento(self):
        """Prueba con una lista de un solo elemento"""
        resultado = self.objeto.ObtieneMasBailable([0.5])
        self.assertEqual(resultado, 0.5)
    
    def test_ObtieneMasBailable_con_negativos(self):
        """Prueba con números negativos"""
        resultado = self.objeto.ObtieneMasBailable([-5, -2, -8, -1])
        self.assertEqual(resultado, -1)
    
    # ==================== Pruebas para VerificaListaCanciones ====================
    
    def test_VerificaListaCanciones_lista_vacia(self):
        """Prueba con una lista vacía (debería retornar True)"""
        resultado = self.objeto.VerificaListaCanciones([])
        self.assertTrue(resultado)
    
    def test_VerificaListaCanciones_none_al_inicio(self):
        """Prueba con None al inicio de la lista"""
        resultado = self.objeto.VerificaListaCanciones([None, "Canción 2", "Canción 3"])
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
