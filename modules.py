import os
import math
directorio_actual = os.getcwd()
print(f"Directorio actual: {directorio_actual}")
def logent():
    ent = int(input("Enter an integer: "))
    logente = math.log2(ent)
    print(f"Log base 2 of {ent} is: {logente}")
    piso = math.floor(logente)
    techo = math.ceil(logente)
    print(f"floor: {piso}")
    print(f"Ceiling: {techo}")
logent()