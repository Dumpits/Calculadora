salir = False
while salir == False:
    num1 = int(input("numero 1: "))
    salir2 = False
    cadena = str(num1)
    while salir2 == False:

        num2 = int(input("numero 2: "))
        condicion = input("¿quieres +, -, / o *?")

        cadena = "(" + cadena + " " + condicion + " " + str(num2) + ")"

        if condicion == "+":
            num1 = num1 + num2
            print(num1)
        elif condicion == "-":
            num1 = num1 - num2
            print(num1)
        elif condicion == "/":
            num1 = num1 / num2
            print(num1)
        elif condicion == "*":
            num1 = num1 * num2
            print(num1)
        else:
            print("Introduzca una opción correcta")

        salir3 = False
        while salir3 == False:
            condicion = input("¿Quieres seguir calculando (calcular), ver el historial (historial), reiniciar la calculadora (reiniciar) o apagar el programa (apagar)")

            if condicion == "calcular":
                salir3 = True
            elif condicion == "historial":
                print(cadena)
            elif condicion == "reiniciar":
                salir3 = True
                salir2 = True
            elif condicion == "apagar":
                salir3 = True
                salir2 = True
                salir = True
            else:
                print("Introduzca una opción correcta")