number_array = [-3,1,2,11,14,25,100]
new_array = []

for i in number_array:
    if i > 5:
        new_array.append(i+2)

print(f"Original Array: {number_array}")
print(f"New Array: {new_array}")