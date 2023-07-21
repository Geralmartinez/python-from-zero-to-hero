# una evaluación condicional puede estar dentro de otra:

name = input("hola, cuál es tu nombre? ")
age = int(input("dime tu edad"))

if age >= 18:
    drink = input("¿quieres cerveza o vino?")
    print("toma", name)
    if drink == "cerveza":
        print("aqui tienes tu cerveza")
    else:
        print("aqui está tu vino")
else:
    juice = input("¿quieres jugo de frutilla o naranja?")
    print("Toma", name)
    if juice == "frutilla":
        print("acá esta tu jugo de frutilla")
    else:
        print("aqui tienes tu jugo de naranja")