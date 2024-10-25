"""
8. Write a program that generates random 4 digits number of 0s and 1s and
convert the generated number to base 10.
"""
import random

rand_dig = []
for _ in range(4):
    rand_dig.append(random.randint(0, 1))

bin = "".join(str(num) for num in rand_dig)
print(f"Four random digits: {bin}")
print("Converting to base 10...")
print(int(bin, 2))
