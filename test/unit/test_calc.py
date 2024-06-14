import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


#@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    #Suma
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        
    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add,"2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        
    #Resta
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(-4, self.calc.substract(-2, 2))
        self.assertEqual(1, self.calc.substract(1, 0))
        
    def test_substract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.substract,"2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())
    
     #Multiplicación  
    #@patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self):#, _validate_permissions):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        
    #@patch('app.util.validate_permissions', side_effect=mocked_validation, create=True)
    def test_multiply_method_returns_correct_result(self):#, _validate_permissions):
        #self.assertEqual(TypeError, self.calc.multiply("2", 2))
        #self.assertEqual(TypeError, self.calc.multiply(1, "0"))
        #self.assertEqual(TypeError, self.calc.multiply("-1", "0"))
        #self.assertEqual(TypeError, self.calc.multiply(None, 2))
        #self.assertEqual(TypeError, self.calc.multiply(2, None))
        #self.assertEqual(TypeError, self.calc.multiply(object(), 2))
        #self.assertEqual(TypeError, self.calc.multiply(2, object()))
        self.assertRaises(TypeError, self.calc.multiply,"2", 2)
        self.assertRaises(TypeError, self.calc.multiply,1, "0")
        self.assertRaises(TypeError, self.calc.multiply,"-1", "0")
        self.assertRaises(TypeError, self.calc.multiply,None, 2)
        self.assertRaises(TypeError, self.calc.multiply,2, None)
        self.assertRaises(TypeError, self.calc.multiply,object(), 2)
        self.assertRaises(TypeError, self.calc.multiply,2, object())
        
    #Divición  
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)
        self.assertRaises(TypeError, self.calc.divide, "0", 0)
    
    
#Potencia
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(4, self.calc.power(-2, 2))
        self.assertEqual(1, self.calc.power(1, 0))
        
    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "2", "2")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())
    
    #Raíz Cuadrada
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(1.4142135623730951, self.calc.sqrt(2))
        self.assertEqual(0.0, self.calc.sqrt(0))
        
    def test_sqrt_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt,"2")
        self.assertRaises(TypeError, self.calc.sqrt,-2)
        self.assertRaises(TypeError, self.calc.sqrt,None)
        self.assertRaises(TypeError, self.calc.sqrt,object())
        
    #Logaritmo Base 10  
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0.3010299956639812, self.calc.log10(2))
        
    def test_log10_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.log10,"2")
        self.assertRaises(TypeError, self.calc.log10,-2)
        self.assertRaises(TypeError, self.calc.log10,0)
        self.assertRaises(TypeError, self.calc.log10,None)
        self.assertRaises(TypeError, self.calc.log10,object())
        
    #Función checa numeros
    def test_check_types_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.check_types, "2", 2)
        self.assertRaises(TypeError, self.calc.check_types, 2, "2")
        self.assertRaises(TypeError, self.calc.check_types, "2", "2")
        self.assertRaises(TypeError, self.calc.check_types, None, 2)
        self.assertRaises(TypeError, self.calc.check_types, 2, None)
        self.assertRaises(TypeError, self.calc.check_types, object(), 2)
        self.assertRaises(TypeError, self.calc.check_types, object())
        self.assertRaises(TypeError, self.calc.check_types, None)
        self.assertRaises(TypeError, self.calc.check_types, "2")
    
    


        
   
if __name__ == "__main__":  # pragma: no cover
    unittest.main()
