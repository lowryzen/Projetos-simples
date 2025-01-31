# Banco de dados

def banco_dados():
    while True:
        nome = str(input("Digite seu nome: ".strip())).capitalize()
        idade = int(input("Digite sua idade: ".strip()))
        genero = str(input("Digite seu gênero: ").strip()).capitalize()

        pessoas_cadastradas = []

        if genero not in ["Masculino", "Feminino"]:
            print ("Gênero inválido")
            break
        else:
            pessoas_cadastradas.append(nome)

        with open ("dados.txt", "a") as dados:
            dados.write(f"\n{nome}, {idade} anos, gênero: {genero}")

        continuar = str(input("Deseja inserir mais dados?: ")).capitalize()
        if continuar == "Sim":
            continue
        else:
            print (f"Foram cadastradas {len(pessoas_cadastradas)} pessoa(s)")
            break


if __name__ == "__main__":
    banco_dados()