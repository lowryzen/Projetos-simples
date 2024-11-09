#Calculadora 1.0

try:
   def soma():
       return a + b
   def subtração():
      return a - b
   def multiplicação():
      return a * b
   def divisão():
      return a / b
   
   a = int(input())
   x = str(input())
   b = int(input())

   if x == ("mais"):
      print (soma())
   elif x == ("+"):
      print (soma())

   elif x == ("menos"):
      print (subtração())
   elif x == ("-"):
      print (subtração())

   elif x == ("vezes"):
      print (multiplicação())
   elif x == ("x"):
      print (multiplicação())
   
   elif x == ("dividido"):
      print (divisão())
   elif x == ("/"):
      print (divisão())
   
   else:
      print ("Na segunda pergunta, use uma das operações matemáticas.")
   

except ValueError as erro:
   print ("Digite apenas numeros.")
except ZeroDivisionError as erro2:
   print ("Não é possivel dividir por zero.")

