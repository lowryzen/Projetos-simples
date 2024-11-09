# verificador de email e senha 1.0

email = str(input("insira seu email: "))
senha = input("insira sua senha:")

dominio = "@gmail.com"

dominio_final = (email + "@gmail.com")

email_final = input("insira seu email novamente:")
senha_final = input("insira sua senha:")

if email_final == dominio_final:
    if senha_final == senha:
        print ("você entrou com sucesso")
else:
    print ("email ou senha incorretos")

