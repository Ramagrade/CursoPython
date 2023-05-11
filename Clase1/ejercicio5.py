nota = int(input("Ingrese una nota entre 0 y 10: "))

while nota <0 or nota >10:
    nota = int(input("Número erróneo, ingrese una nota entre 0 y 10: "))
print(nota)