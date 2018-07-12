"""To practise comprehension list"""

a = [1, 2, 3, 4]
filter_even_list = []
for item in a:        # 1st Iter item = 1 , 2nd item = 2
    if item % 2 == 0:   # 1 == 0 -> False , 0 == 0 True
        filter_even_list.append(item)     # [].append(2) -> [ 2 ]

print(filter_even_list)   # [ 2, 4 ]

filter_even_list_lc = [item for item in a if item % 2 == 0]

print(filter_even_list_lc)  # [ 2, 4]

a = "python"
print([vowel for vowel in a if vowel in "aeiou"])

a = [[1, 2, 3],
     [10, 20, 30],
     [40, 50, 60],
     ]
#
temp_list = []
for item_list in a:   # 1st item_list = [1, 2, 3]  item_list = [10, 20 , 40]
    # print(item_list[1])   # [1, 2, 3] [1] -> 2  item_list[1] -> 2
    temp_list.append(item_list[2])

print(temp_list)  # [3, 30 , 60)
print([item_list[2] for item_list in a])


temp_list = []
for item_list in a:
    for item in item_list:
        temp_list.append(item * 4)

print(temp_list)

print([item*4 for item_list in a for item in item_list])

a = [[1, 2, 3],
     [10, 20, 30],
     [40, 50, 60],
     ]

re_datatype = {item: item*4 for item_list in a for item in item_list}  # [1, 2, 3]  # 1
print(re_datatype)
print(type(re_datatype))

re_datatype = {item for item_list in a for item in item_list}
print(re_datatype)
print(type(re_datatype))

re_datatype = (item for item_list in a for item in item_list)
print(re_datatype)
print(type(re_datatype))



# 1
# 2
# 3


final_item = []
for item in range(5):
    for item2 in range(5):
        if 1 < item != 4:
            final_item.append(item2)

print(final_item)


list1 = [item2 for item in range(5) if 1 < item != 4 for item2 in range(5) ]
print(list1)

a = [2, 1, 4, 3, 5, 0]
print(a[a[4]])  # a[4] -> a[4] -> 4
print(a[a[3]])  # a[a[3]] -> a[3]  -> 3

