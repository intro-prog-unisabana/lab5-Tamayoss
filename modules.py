import os
import math
Current_working_directory = os.getcwd()
print(f"Directorio actual: {Current_working_directory}")
def logent():
    ent = int(input("Enter an integer: "))
    logente = math.log2(ent)
    print(f"Log base 2 of {ent} is: {logente}")
    Floor = math.floor(logente)
    Ceiling = math.ceil(logente)
    print(f"floor: {Floor}")
    print(f"Ceiling: {Ceiling}")
logent()