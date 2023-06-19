fries123 = input("Escolha 3 números separados por espaços: ")

numeros = fries123.split()
numero1 = int(numeros[0])
numero2 = int(numeros[1])
numero3 = int(numeros[2])

minimo = min(numero1, numero2, numero3)
maximo = max(numero1, numero2, numero3)
media = (numero1 + numero2 + numero3) / 3

print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Média:", round(media))

