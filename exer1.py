# Scripts/activate
# python *nome do arquivo.ext*
# python -m unittest *nome do arquivo.ext*

import unittest

def salario_com_desconto_inss( valor_hora: float, num_aulas: float, percent_inss: float ):
    valor_init = valor_hora * num_aulas
    desconto = valor_init * ( percent_inss / 100 )
    valor_final = valor_init - desconto
    return valor_final

# Programa principal
class SalarioLiquido( unittest.TestCase ):
    def test_sor_1( self ):
        self.assertEqual( salario_com_desconto_inss( 6.25, 160, 1.3 ), 987.00 )
    
    def test_sor_2( self ):
        self.assertEqual( salario_com_desconto_inss( 20.5, 240, 1.7 ), 4836.36 )

    def test_sor_3( self ):
        self.assertEqual( salario_com_desconto_inss( 20.5, 240, 1.7 ), 4836.36 )

if __name__ == '__main__':
    unittest.main