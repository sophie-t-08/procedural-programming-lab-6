def find_first_even_number(numbers):
    for num in numbers:
        if num % 2 == 0:
            return num
        else:
            return None
result = find_first_even_number([1, 3, 5, 6, 7, 8])
print(result)
# Doesn't iterate through list

def find_first_even_number(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(i)
        else:
            i = i + 1
print(find_first_even_number([1, 3, 5, 6, 7, 8]))       