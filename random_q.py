import random 

random.seed(123)

entrada = int(input("Enter the start value:\n"))
salida = int(input("Enter the end value:\n"))
aleatorio = random.randint(entrada, salida)
print(f"Generated random number: {aleatorio}")