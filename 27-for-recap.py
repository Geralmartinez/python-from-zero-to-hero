#el for es una estroctura que sirve para ejecutar un conjunto de sentencias por cada elemento de una colección.ademas el for no da una variable para acceder en cada vuelta al elemento que corresponde.

banana = "esto es un ejemplo"

#esta es la forma manual carretera ordinaria, picante vulgar
print(banana[0])
print(banana[1])
print(banana[2])
print(banana[3])
print(banana[4])
print(banana[5])
print(banana[6])

print("---------------------------------")

# está es la forma pirula, elegante o correcta de correr el texto usando un while

position = 0
last_position = 18

while position < last_position:
    print(banana[position])
    position = position + 1

print(position)

print("------------------------------")

#esta la forma mas cencilla, elegante o pythonezca de recorrer un string
for letter in banana:
    print(letter)