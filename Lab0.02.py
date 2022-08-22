'''
############
# Lab 0.02 #
############

In this lab, we will create a Pet class that will keep track of the type of animal, 
color, food, noise and name of a given animal.

Create a class called Pet that has the following attributes
Animal (e.g., dog, cat, fish)

Color (e.g., spotted, tabby, gold)

Food (e.g., kibbles, tuna, fish flakes)

Noise (e.g., meow, woof, splash)

Name (e.g., Scooby Doo, Fluffy, Bubbles)

Specifications
--------------
Make sure to use the __init__ method to create these attributes.

Create a list of pets.

Create a function that takes in a list of pets and prints out the name 
and the food attributes.

Test your function with your list of pets.
'''
# class that instantiates a pet object
class Pet():
    def __init__(self, animal, color, food, noise, name):
        self.animal = animal
        self.color = color
        self.food = food
        self.noise = noise
        self.name = name

# function that takes in a list of pets and prints their name and food type
def pet_info(list_of_pets):
    for pet in list_of_pets:
        print(f"{pet.name} eats {pet.food}.")

# instances of the Pet class
pet1 = Pet('dog', 'black', 'dog chow', 'ruff', 'Allie')
pet2 = Pet('cat', 'brown', 'salmon', 'meow', "Katie Kat")
pet3 = Pet('fish', 'silver', 'vegetation', 'bloop bloop', 'Charlie')
pet4 = Pet('snake', 'copper', 'mice', 'ssssss', 'Legless')

# list of pet objects
PET_LIST = [pet1, pet2, pet3, pet4]

# call the pet info function to output each pets name an food attributes
pet_info(PET_LIST)



