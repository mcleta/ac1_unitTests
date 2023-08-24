import unittest

def lista_vFinal_e_desconto( valor_produto: float ):
    desconto = valor_produto * 0.09
    valor_final = valor_produto * 0.91
    lista = [ valor_final, desconto ]
    return lista

# Programa principal
class ValorFinalEDesconto( unittest.TestCase ):
    def test_produto_1( self ):
        self.assertEqual( lista_vFinal_e_desconto( 100 ), [ 91.00, 9.00 ] )

    def test_produto_2( self ):
        self.assertEqual( lista_vFinal_e_desconto( 1500 ), [ 1365.00, 135.00 ] )

    def test_produto_3( self ):
        self.assertEqual( lista_vFinal_e_desconto( 60000 ), [ 54600.00, 5400.00 ] )

if __name__ == '__main__':
    unittest.main