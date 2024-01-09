import time

class MyRandomGenerator:
    def __init__(self, seed=None):
        # Choose initial seed based on current time if not provided
        self.seed = seed if seed is not None else int(time.time() * 1000)
        self.state = self.seed

    def _generate_next(self):
        # LCG parameters (example values)
        a = 1664525
        c = 1013904223
        m = 2**32

        # Generate the next state using the LCG formula
        self.state = (a * self.state + c) % m

        # Return a normalized random value in the range [0, 1)
        return self.state / m

    def random(self):
        return self._generate_next()

# Example usage:
my_rng = MyRandomGenerator()
random_number = my_rng.random()

print("Random number:", random_number)

