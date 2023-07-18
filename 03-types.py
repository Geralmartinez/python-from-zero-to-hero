#podemos pensar que en python todo es un valor, valores que hemos visto son:
#"hola mundo", 2, 4, "harvys" . todos los valores tienen un TIPO y depende del tipo las opera

# para ver el tipo de un valor, tenemos la función type()

print(type("hola mundo")) # los texto son de tipo string o str
print(type(2)) # los números enteros son de tipo int
print(type(3.2)) # los números con parte decimal son float


phrase_one = "hola mundo" 

#le pasamos a print una operacion con valores. estamos "sumando" textos
print(phrase_one,phrase_one)

#multiplicar texto
print(phrase_one * 3)

#pero no podemos sumar textos con números
#print(phrase_one + 4)
#print(phrase_one/phrase_one)