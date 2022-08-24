def merge_sort(list):
    if len(list) <= 1:
        return list
    mid_Point = int(len(list) / 2)
    left, right = merge_sort(list[:mid_Point]), merge_sort(list[mid_Point:])
    return merge(left, right)
def merge(left, right):
    result = []
    left_pointer = right_pointer = 0
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1
    result.extend(left[left_pointer:])
    result.extend(right[right_pointer:])
    return result


def list_input():
    list = []
    n = int(input("enter no. of elements : "))
    for i in range(n):
        element = int(input("enter numbers : "))
        list.append(element)
    print("sorted list :",list)
    result = merge_sort(list)
    print( "sorted list :", result)

list_input()