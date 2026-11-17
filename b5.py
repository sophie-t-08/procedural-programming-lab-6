def minimum(lst):
    a = 0
    for x in range(1, len(lst)):
        if lst[x] < lst[a]:
            a = x
    return a
print(minimum([4, 2, 7, 3]))
# Error - prints minimum index instead of minimum value because a is 0 and has no iteration statement to iterate through the list and find the minimum value, hence is always compared to 0.


def minimum(lst):
    min_value = lst[0]
    for x in range(1, len(lst)):
        if lst[x] < min_value:
            min_value = lst[x]
    return min_value
print(minimum([4, 2, 7, 3]))