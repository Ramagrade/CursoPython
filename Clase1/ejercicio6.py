genero = input("ingrese su género, f o m: ")

while genero != "f" and genero != "m": 
    input("genero no válido, por favor ingrese su género, f o m: ")
if  genero == "m":
    print("sos hombre")
else: print("sos mujer")