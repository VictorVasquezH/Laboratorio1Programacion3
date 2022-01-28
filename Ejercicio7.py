peso = float( input('Ingrese su peso en KG: '));
estatura = float(input('Ingrese su estatura en Metros: '));
total = (peso / (pow(estatura, 2)))

print('Su peso corporal es de: ',"{:.2f}".format(total))