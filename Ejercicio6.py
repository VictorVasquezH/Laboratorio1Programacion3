numero = int (input ('Ingrese el numero: '));

if numero >=0:
    total = str (((numero + 1 )*numero) / 2)
    print("El resultado es: ", total)

else:
    print("Ingrese un numero positivo.")
