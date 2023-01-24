def check_sublist(lst, sub):
    for i in range(len(lst) - len(sub) + 1):
        if lst[i:i+len(sub)] == sub:
            return True
    return False

list1 = [1, 2, 3, 4, 5]
list2 = [2, 3]
list3 = [6, 7, 8]

print(check_sublist(list1, list2)) # True
print(check_sublist(list1, list3)) # False
