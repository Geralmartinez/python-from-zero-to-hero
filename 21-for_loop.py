import time
#python los string ya son varios valores en uno. cada string está conpuesto de caracter o letras
some_text = "algún texto de ejemplo"
#en un texto podemos acceder a cada letra utilizando los [] e indicado su posición partiendo desde 0
print(some_text[0]) #a
print(some_text[1]) #l
print(some_text[2]) #g

# en python los string son colecciones de cracteres. veremos otras colecciones más adelante, como listasy los diccionarios
#las colecciones las podemos recorrer con el loop for que va a ejecutar su cuerpo una vez por cada elementode la colección

for letter in some_text:
    print(letter)

for num in range(-10,1):
    print(-1 * num)
    time.sleep(1)
print("boom")