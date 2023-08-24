import unittest

def lista_vFinal_e_vComissao( valor_produto: float ):
    comissao = valor_produto * 0.1
    valor_final = valor_produto + comissao
    lista = [ round(valor_final, 2), round(comissao, 2) ]
    return lista

# Programa principal
class ValorFinalEDesconto( unittest.TestCase ):
    def test_conta_1( self ):
        self.assertEqual( lista_vFinal_e_vComissao( 75 ), [ 82.50, 7.5 ] )

    def test_conta_2( self ):
        self.assertEqual( lista_vFinal_e_vComissao( 125 ), [ 137.50, 12.5 ] )

    def test_conta_3( self ):
        self.assertEqual( lista_vFinal_e_vComissao( 350.87 ), [ 385.96, 35.09 ] )

if __name__ == '__main__':
    unittest.main