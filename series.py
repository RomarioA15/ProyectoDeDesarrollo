def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

def calculadora():
    print("Calculadora Simple")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Seleccione una operación (1-4): ")
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == '1':
        print("Resultado:", suma(num1, num2))
    elif opcion == '2':
        print("Resultado:", resta(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == '4':
        print("Resultado:", division(num1, num2))
    else:
        print("Opción inválida")

if __name__ == "__main__":
    calculadora()