#Camara de teste 2

def popup():
    from tkinter import Label, Tk

    janela = Tk()
    janela.title("despertador")
    texto = Label(janela, text="Já deu o horário nengue", font=("Heavitas", 40))
    texto.pack()

    janela.mainloop()

def despertador():
    try:
        import time

        relogio = int(input("Vai despertar daqui a quantos segundos 🤨: "))

        if relogio <= 3600:
            for cadasegundo in (range(relogio)):
                segundos = cadasegundo % 60
                minutos = int(cadasegundo / 60) % 3600
                time.sleep(1)
                print(f"{round(minutos):02}:{round(segundos):02}")
            popup()
        else:
            print("Limite temporário de 1 hora.")

    except ValueError:
        print("Insira apenas números")

if __name__ == "__main__":
    despertador()