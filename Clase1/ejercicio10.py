numeros = [3,5,2,8,1,9,4,10]
pares = []
impares = []
for numero in numeros:
    if(numero % 2 == 0):
        pares.append(numero)
    else: impares.append(numero)
print (f"hay 4 pares, y esos son: " + (str(len(pares))))
print (f"hay 4 impares, y esos son: " + (str(len(impares))))