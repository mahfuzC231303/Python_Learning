print(list(range(1, 11)))  # This will print numbers from 1 to 10

for i in range(100):
    print("my name is mahfuz")
    print(i)


for i in range(1,101):
    print(i**2)  # This will print the square of numbers from 1 to 100


# Task1: take an empty list and append all even numbers from 0 to 100 in it. Then print the list.
empty_list = []
for i in range(0,101,2):
    empty_list.append(i)

print(empty_list)  # This will print all even numbers from 0 to 100

#2nd way:
my_list =[]
for i in range(101):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)  # This will print all even numbers from 0 to 100

#3rd way:
nums=[i for i in range(0,101,2)] # List comprehension to create a list of numbers from 1 to 100
print(nums)  # This will print numbers from 1 to 100


#Task2: print the maximum and minimum number and sum of all numbers from the list of 0 to 100.
print(max(empty_list))  # This will print the maximum number from the list
print(min(empty_list))  # This will print the minimum number from the list
print(sum(empty_list))  # This will print the sum of all numbers from the list


#---------------------------------------------------------------------------------------#



# Below this codes are for for learning purpose. You can uncomment them to see the output.

# for i in range(6):
#     for j in range(i):
#         print("*", end="")
#     print(" ") # This will print a triangle of asterisks

# for i in range(4):
#     for j in range(4-i):
#         print("*", end="")
#     print(" ") # This will print an inverted triangle of asterisks