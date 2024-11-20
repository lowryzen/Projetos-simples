#Camara de teste 2

def calculadora():
    try:
        a = int(input("Primeiro número: "))
        x = str(input("Operação matemática: "))
        b = int(input("Segundo número: "))

        operacao ={"+": a + b, "mais": a + b,
        "-": a - b, "menos": a - b,
        "x": a * b, "vezes": a * b,
        "/": a / b, "dividido por": a / b}

        if x in operacao:
            print (operacao[x])
        else:
            print ("Operação inválida")

    except ValueError:
        print ("Digite números")
    except ZeroDivisionError:
        print ("Não é possível dividir por zero")

if __name__ == "__main__":
    calculadora()








