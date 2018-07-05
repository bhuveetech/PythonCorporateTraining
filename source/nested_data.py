""" This is for nested data examples"""
c = "python"
print(c[2])  # t
print(id(c[2]))
print(id("t"))
print(id(c[2]) == id("t"))  # True
print(c[2] is "t")  # True

list1 = ["ab", 1, 1.2, [1, 4], {"name": "ab",
                                "name2" : "yz",
                               "payload" : {"data1":1,
                                          "data2": 2,
                                            "data3":[1, 2, 3, "naresh", [1, 2, 3],
                                                     {"sub_data":[34,23]}
                                                     ]
                                            }

                               }
         ]

print(list1[4]["payload"]["data3"][3][-1]) # h
print(list1[4]["payload"]["data3"][5]["sub_data"][1]) # 23


print(list1[0])   # "ab"
print(list1[0][0]) # "ab"[0] -> a
print(list1[0] is list1[4]['name']) # True

print(list1[3])  # [1, 4 ]
print(list1[3][0]) # 1


print(list1[4])  #
print(list1[4]["name"][0])  # a

print(list1[4]["name2"][1])  # "yz"[1] -> z
print(list1[4]["payload"]["data1"])  # 1


