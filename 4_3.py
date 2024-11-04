import random

num_elements = random.randint(3, 10)
original_list = [random.randint(1, 100) for _ in range(num_elements)]
new_list = [original_list[0], original_list[2], original_list[-2]]

print("Оригінальний список:", original_list)
print("Новий список:", new_list)
