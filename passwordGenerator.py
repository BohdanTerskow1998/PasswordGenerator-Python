import random
import string

stringNumber = int(input())


class PasswordGenerator:
    def __init__(self, n):
        self.n = n

    def generate_random_string(self):
        letters = string.hexdigits
        rand_string = ''.join(random.choice(letters) for i in range(self.n))
        print("Result: ", rand_string)


generator = PasswordGenerator(stringNumber)
generator.generate_random_string()
