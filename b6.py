def total_sum(lst):
    for x in lst:
        total = 0
        total = x + total
    return total
print(total_sum([1, 2, 3, 4]))
# error occurs as it prints the adds 0 to index so total will equal to the end value being 4.

def total_sum(lst):
    total = 0
    for i in lst:
        total += i
    return total
print(total_sum([1, 2, 3, 4]))