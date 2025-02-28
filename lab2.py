# 1.Write a program to check if 'apple' is present in the set {'apple', 'banana', 'cherry'}
fruits = {'apple', 'banana', 'cherry'}
print('apple' in fruits)  

# 2.Length of a Set:
# Find the length of the set numbers = {10, 20, 30, 40, 50}.

numbers = {10, 20, 30, 40, 50,80,90,87}
length = len(numbers)  
print(length)

# 3.Remove Duplicates from a List:
# Write a program to remove duplicates from the list [1, 2, 2, 3, 4, 4, 5] using a set.

num_list = [1, 2, 2, 3, 4, 9, 9, 4, 9, 4, 5]
unique_numbers = list(set(num_list))
print(unique_numbers)
