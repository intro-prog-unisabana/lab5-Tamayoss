from utils import *

mensaje = input("Please type your message\n")

menvolteado = flip(mensaje)
contar = count_letters(mensaje, "a")

print(f"Your encoded message is: {menvolteado}{contar} ")
    

