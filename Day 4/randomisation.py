import random
# import my_module

random_integer = random.randint(1, 20)
print(random_integer)

# print(my_module.my_favourite_number)

random_number_0_to_1 = random.random()
print(random_number_0_to_1)

random_number_0_to_10 = random.random() * 10 # Multiplying it by 10 to make its range wider
print(random_number_0_to_10)

random_float = random.uniform(0, 10)
print(random_float)