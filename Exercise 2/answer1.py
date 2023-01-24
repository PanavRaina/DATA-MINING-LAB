lists = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
max_sum = 0
max_list = []
for lst in lists:
    if sum(lst) > max_sum:
        max_sum = sum(lst)
        max_list = lst
print(max_list)
