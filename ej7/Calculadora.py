class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b

    @staticmethod
    def restar(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

print("Suma:", Calculadora.sumar(10, 5))
print("Resta:", Calculadora.restar(10, 5))
print("Multiplicación:", Calculadora.multiplicar(10, 5))
print("División:", Calculadora.dividir(10, 5))
print("División por cero:", Calculadora.dividir(10, 0))
