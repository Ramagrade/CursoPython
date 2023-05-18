numeros= [23, -14, 0, 0, 21, -9, -5, 34, 89]
contPos= 0
contNeg= 0
contCeros= 0
for numero in numeros:
    if (numero == 0):
        contCeros = contCeros + 1
    elif(numero > 0):
        contPos += 1
    else:
        contNeg += 1
print("Ceros: ", contCeros)
print("Positivos: ", contPos)
print("Negativos: ", contNeg)