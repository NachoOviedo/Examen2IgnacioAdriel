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
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()