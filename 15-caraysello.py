import random

computer_choice =  random.choice(["cara", "sello"])
user_option = input("escoja entre cara y sello: ")

if computer_choice == user_option:
    print("el computador tiro: ", computer_choice)
    print("¡EMPATE!")
elif computer_choice == "cara" and user_option == "sello":
    print("el computador tiro: ", computer_choice)
    print("!Ganaste¡") 
else:
    print("el computador tiro: ", computer_choice)
    print("!PERDISTE¡")