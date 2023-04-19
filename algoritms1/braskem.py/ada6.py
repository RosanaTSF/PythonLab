x = int(input("Digite um número inteiro: "))

if x < 0:
    resp1 = "negativo"

else:
    resp1 = "positivo"
    
if x % 2 == 0:
    
    resp2 = "par"

else:
    resp2 = "impar"
    

print("O número {} é {} e {}.".format(x, resp1, resp2))