# Treino com decoradores

def operacoes(func):
    def wrapper(a, b):
        try:
            sinal = {
                "+": a + b,
                "-": a - b,
                "x": a * b,
                "/": a / b
            }

            resposta = input(str("Selecione uma operação: "))
            print(sinal[resposta]) if resposta in sinal else print("Use somente +,-,* ou /")
            print(f"A raiz quadrada de sua resposta é: {(sinal[resposta] ** 0.5)}")

            func(a, b)

        except ZeroDivisionError:
            print("Não é possivel dividir por zero")
        except ValueError:
            print ("Ta dando calculo errado mané")

    return wrapper


@operacoes
def numeros(a, b):
    print(f"Os números escolhidos são: {a, b}")


if __name__ == "__main__":
    numeros(20,10)
