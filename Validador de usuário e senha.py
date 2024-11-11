#Validador de nome de usuário e senha

print ('''Instruções: Seu nome de usuário não pode ter mais que 12 letras,
não pode ter espaço e nem números''')

print ("Sua senha precisa ter no mínimo 8 caracteres, um dígito e um caractere especial")

def validador():
    try:
        usuario = (input("Seu nome de usuário: "))
        if usuario.isalpha() == True and len(usuario) < 12 :
            pass
            senha = input("Sua senha: ")
            if len(senha) >= 8 and senha.find('1'):
                print ("Sucesso")
            else:
                print ("Sua senha precisa seguir as instruções")
        else:
            print("Nome de usuário invalido")

    except ValueError as erro:
        print('Algo deu errado', str(erro))

validador()
