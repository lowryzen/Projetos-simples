# Treino com decoradores

def operacoes(func):
    def wrapper(a,b):
        sinal = {
            "+": a+b,
            "-":a-b,
            "x": a*b,
            "/": a/b
        }
        resposta = input(str("Selecione uma operação: "))
        if resposta in sinal:
            print(sinal[resposta])
        func(a,b)
    return wrapper

@operacoes
def numeros(a,b):
    print (f"Os números escolhidos são: {a,b}")

numeros(15,3)