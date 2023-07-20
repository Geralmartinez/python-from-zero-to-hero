import random
#programar con estructuras de control y expreciones booleanas un juego cachipún

computer_choice = random.choice(["piedra", "papel", "tijera"])
print("Bienvenidos al juego cachipun")
user_option = input("escoje entre piedra, papel, tijera: ")

if user_option == computer_choice:
    print("la opción del computador es: ",computer_choice)
    print("¡EMPATE!")
elif (user_option == "tijera" and computer_choice == "papel") or (user_option == "piedra" and computer_choice == "tijera") or (user_option == "papel" and computer_choice == "piedra"):
    print("la opción del computador es: ",computer_choice)
    print("¡GANASTE!")
else:
     print("la opción del computador es: ",computer_choice)
     print("¡PERDISTE!")
