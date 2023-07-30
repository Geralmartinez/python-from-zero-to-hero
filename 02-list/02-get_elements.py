# get obtener
#para acceder a un elemento de la lista se usa el nombre de la variable seguido de [] indicando en su interior la posición  del elementopartiendo de cero.

fruits = ["pineapple","banana", "orange"]

print(fruits[0])
print(fruits[-1])

#ATENCIÓN
# podemos modificar un elemento de la lista de la sigente forma
# es decir, necesitamos utilizar el indice
fruits[1] = "chocolate"
# PRECAUSÓN. lo anterior borra el valor que avia previamente

print(fruits)