import random

class MyRandomGenerator:
    def generate_random(self):
        # Use the random module from the standard library
        return random.random()

# Example usage:
my_rng = MyRandomGenerator()
random_number = my_rng.generate_random()

print("Random number:", random_number)
