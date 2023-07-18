# hacer un programa de determine el perimetro de una torta en centimetros
# nota para el valor de pi, utilizar 3.14
# el usuario del programa ingresará mediante el teclado el radio de la torta

def calcular_perimetro_torta(diametro):
    pi = 3.14
    perimetro = pi * diametro
    return diametro
diametro_torta = float(input("ingresa el diametro de la torta en centimetros:"))
perimetro_torta = 3.14
calcular_perimetro_torta(diametro_torta)
print("el perimetro de la torta es:", perimetro_torta ,"centimetros")
