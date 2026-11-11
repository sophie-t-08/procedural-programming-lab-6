list1 = []
list2 = []

def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements
print(find_common_elements(list1, list2))