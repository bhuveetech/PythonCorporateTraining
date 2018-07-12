"""For practising conditional statements"""

# =========== if , elif, else ================= #
a = 11

if a < 10:
    print("It's less than 10")

elif 10 <= a < 20:
    print("It's between 10 and 20")

elif 20 < a <= 50:
    print("It's between 20 and 50")

else:
    print("It's more than 50")


# ======================= Implement Ternary Operator =========== #
a = 20
b = 2
print(a) if a < b else print(b)

# ============== While ======================= #
a = 1

while a < 10:
    print(a)   #  1, 2 , 3, 4,5,  6, 7, 8, 9
    a += 1   #  a = a + 1

else:
    print("outside pass")

print("Comman statements")


# ================== for ====================== #
lan = "python"
list1 = [1, 2, 3, 4]
tuple1 = (20, "xyz", [2, 3])
dict1 = {"name1": "xyz",
        "name2": "yz"}

set1 = {1, 3, 4, 5, 10}


for target in lan:
    print(target)  # p, y, t, h, o , n


for target in list1:
    print(target)     # 20 , "xyz" , [2,3]

for target in dict1:
    print(target)     # "name1" "name2"
    print(dict1[target])

for target in set1:
    print(target)

else:
    print("Outside of loop:{}".format(target))


# ============= Pass statement =========== #
a = 1
if a:
    pass
















