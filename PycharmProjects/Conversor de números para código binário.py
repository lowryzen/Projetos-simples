#Camara de teste 2

def count_bits(n):
    binary = []
    while True:
        binary.append(int(n%2))
        n/=2
        if n<1:
            binary = binary[::-1]
            break
    print (binary)

count_bits(7)