# verificador de email e senha 1.1

def email():
    bloco1 = str(input("Seu nome: "))
    bloco2 = input("Sua senha:")

    bloco_email = bloco1 + "@gmail.com"

    verificador = input("Digite seu email completo: ")
    verificador2 = input("Digite sua senha novamente: ")

    if verificador == bloco_email:
        if verificador2 == bloco2:
            return "Você logou com sucesso."
        else:
            return "Email ou senha incorretos"
    else:
        return "Email ou senha incorretos"

print (email())

