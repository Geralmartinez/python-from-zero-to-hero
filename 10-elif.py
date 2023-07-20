#podemos en contarsituaciones en que se requiere de más de una evaluación condicional para determinar el flujo de ejecución del programa. esto lo hacemos con la estructura elif que tanbién evalúa una sentencia booleana

first_num = int(input("ingresa el primer número: "))
second_num = int(input("ingresa el segundo número: "))

if first_num > second_num:
    print("El primer número es mayor")
elif first_num < second_num:
    print("El segundo número es mayor")
else:
    print("son iguales")