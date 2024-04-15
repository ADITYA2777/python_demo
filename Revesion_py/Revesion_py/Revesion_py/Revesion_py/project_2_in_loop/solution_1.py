number = [1,-2,-3,4,-5,6,-10,7,8,9]

postive_number_count = 0

for num in number:
    print(num)
    if num > 0:
        postive_number_count += 1
print("final count of postive number is : ", postive_number_count)