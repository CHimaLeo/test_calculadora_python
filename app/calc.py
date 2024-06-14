#from util import validate_permissions
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    #Suma
    def add(self, x, y):
        self.check_types(x, y)
        return x + y
    
    #Resta
    def substract(self, x, y):
        self.check_types(x, y)
        return x - y
    
    #Multiplicación
    def multiply(self, x, y):
 #       if not validate_permissions(f"{x} * {y}", "user1"):
  #            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y
    
    #Divición
    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y
    
    #Potencia
    def power(self, x, y):
        self.check_types(x, y)
        return x ** y
    
    #Raíz Cuadrada
    def sqrt(self, x):
        self.check_types(x)
        if x < 0:
            raise TypeError("Raíz Cuadrada by number negativo is not possible")
        
        return math.sqrt(x)
    
    #Logaritmo Base 10  
    def log10(self, x):
        self.check_types(x)
        if x <= 0:
            raise TypeError("Logaritmo Base 10 by number monores que cero is not possible")
        
        return math.log10(x)

    #Función checa numeros
    def check_types(self, x, y=0):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")


#if __name__ == "__main__":  # pragma: no cover
#    calc = Calculator()
#    result = calc.add(2, 2)
#    print(result)
