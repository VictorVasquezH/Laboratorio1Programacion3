inversion = float (input('Con que cantidad decea epezar a invertir: '));
interes = float (input('De cuanto va a hacer el interes anual: '))
duracion = int (input('Cuantos años decea hacer la iversion: '));

total = str (((inversion * interes/100))*duracion)
print("El total de intereses generados en ",duracion, "años es de: ",total)