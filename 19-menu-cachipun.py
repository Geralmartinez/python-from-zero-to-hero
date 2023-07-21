import random
#crear un juego con cachipún y un menú de opciones
#la opción número 1 será jugar y la opción 2 salir

  

menu_option = 0
while menu_option != 2: #mientras menu_option sea distinto a 2
    menu_option = int(input("ingresa 1 para jugar o 2 para salir"))
    if menu_option == 1:
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