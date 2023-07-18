#prácticamente la totalidad de las aplicaciones y programas computacionalidades realizan las mismas operaciones:
# 1- TOMAR datos desde el exterior como el teclado, el mouse, las redes (internet) u algun otro dispocitivo como sensores o cámaras.

#python trae tanbié una función básica para ingresar datos desde el teclado. la función input()

# 2- SALIDA de datos al exterior como la terminal, un archivo, enviarlo por la red (internet) o un parlante, etc

# python trae para esto la funcion print() que veremos mas en detalle después.

# 3- otra opeción que hace la mayoria de los programas es la EJECUCIÓN CONDICIONAL. que dependiendo de los valores ingresados, ejecuta el programa de cierta forma.
#pyhton trae para esto las ESTROCTURAS DE CONTROL que tan bién conoseremos mas adelante.

# 4- también los programas realizan opereraciones con los valores,ya sea conbinando, sumando, acomulando, calculando, etc .
 
# 5 - Repiticiones: muchas veses para obtener un resultado es necesario repetir pasos sucesivos ( recetas de cocina )

username = input("hola. ¿ cuál es tu nombre?")

print("hola" + username)

if username == "harvys":
    print("¡somos tocayos!")
for letra in username:
    print(letra)