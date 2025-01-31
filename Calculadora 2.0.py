#Calculadora 1.0

def calculadora():
   try:
      a = int(input("digite outro numero:"))
      b = int(input("digite outro numero:"))

      acao = str(input("O que quer fazer com estes numeros?: "))

      operacoes = {
         "soma":        a+b,    "+": a+b,
         "menos":       a-b,    "-": a-b,
         "multiplicar": a * b,  "x": a * b,
         "dividir":     a / b,  "/": a / b
      }

      if acao in operacoes:
         print(operacoes[acao])
      else:
         print("Operação não identificada")

   except ZeroDivisionError:
      print("Não é possível dividir ou multiplicar por zero")

   except ValueError:
      print("Por favor, digite números.")

if __name__ == "__main__":
   calculadora()