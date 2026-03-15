import random 
def seed_secret_numbers(semilla):
    random.seed(semilla)
def generate_secret_number(start =1,end =100):
    return random.randint(start, end)
