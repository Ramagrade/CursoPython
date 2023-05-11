i=0
mayor = None
menor = None
while i < 5:
    numero = int(input("ingrese un número: "))
    
    if i == 0 or numero > mayor:
        mayor = numero
    i += 1

print(f"el mayor es {mayor}")
print(f"el menor es {menor}")