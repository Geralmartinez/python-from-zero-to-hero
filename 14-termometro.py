# pedir al usuario la temperatura
user_tem = int(input("Ingrese la temperatura: "))
# si la temperatura es menor que 0 imprime me congelo
if user_tem <= 0:
    print("Me congelo")
# si la temperatura es entre 1 y 15 imprime tengo frio 
elif user_tem >= 1 and user_tem  <= 15:
    print("Tengo frio")
# si la temperatura esta entre 16 y 25 imprime temperatura ideal
elif user_tem >= 16 and user_tem <= 25:
    print("Temperatura ideal")
# si la temperatura es mayor a 26 tengo calor 
else:
    print("Tengo calor")


