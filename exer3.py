import unittest

def calc_vFinal( valor_produto: float, valor_desconto: float ):
    valor_final = valor_produto - valor_desconto
    return valor_final

# Programa principal
class ValorFinalEDesconto( unittest.TestCase ):
    def test_vFinal_produto_1( self ):
        self.assertEqual( calc_vFinal( 500, 50 ), 450 )

    def test_vFinal_produto_2( self ):
        self.assertEqual( calc_vFinal( 10500, 500 ), 10000 )

    def test_vFinal_produto_3( self ):
        self.assertEqual( calc_vFinal( 90, 0.80 ), 89.2 )

if __name__ == '__main__':
    unittest.main