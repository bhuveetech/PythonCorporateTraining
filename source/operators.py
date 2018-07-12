""" For practising operators examples"""
import copy
# =============== Arithmetic ================ #

a = 4
b = 2

print(a + b)
print(a - b)
print(a / b)  # Python3 2.0 python2 2
print(a // b)
print(a % b)
print(a ** b)

print(3 / 2)    # 1.5
print(3 // 2)   # 1
print(3 // 2.0)  # 1.0

# ============== Assignment Operators ============= #
a = 4
a += 2  # 6  -> a = a + 2
print(a)
a -= 2  # a -= 2  ->  a = a -2 -> 4
print(a)

# ================= Relational Operators ================== #
success_code = 200
response_code = 500
print(1 == 2)
print("python" == "java")

print(response_code == success_code)
print(response_code != success_code)
print(1 > 2)
print(1 < 2)
print(1 >= 2)
print(1 <= 2)
print("java" == "avaj")

# ================== Logical/ Conditional Operators =========== #
status = []   # True
print(status)
print(not "")     # True
print(not 1)      # False
print( not None)  # True
status_code = 500
print([] and 2)  # False > [] -> []
print([] and 2)   # False -> []
print(1 or [] )  # True -> 1

print(status_code >= 400 or status_code < 600)   # True  -> True
print(status_code !=500 and status_code<600)      # False -> False
#
# a = None
# a or print(a)  # None
#
#
# print( status_code >= 400 or status_code >= 500)
#
# a = 1
# a = a+1
# #
# a and a+1 and print(a)
#
# # ==================== Membership Operators ================ #
print("p" in "python")
print("p" not in "python")
print("python" in "p")  # False
print("emp1" in {"emp1":1 , "emp2":2})
print(1 in {"emp1":1 , "emp2":2})  # False Note: key existence
#
#
# # ====================== #
a = 1
b =1
print(a is b)
print(id(a) == id(b))

print(a is not b)  #= Address Identity Operator ============ #
a = 1

list1 = [1, 2, 3]
list2 = copy.deepcopy(list1)
print(list1 is list2)  # False
print(list1 == list2)  # True
#
# # ========================== Bitwise Operators =================== #
a = 1
b = 2
print(a & b)
print(a | b)

print(a << 1)   # 0 0 0 1 << 2 -> 0 0 1 0 -> 3
print(a >> 1)   # 0 0 0 1 >> 2 -> 0 0 0 0 -> 0
#
# ~, ^

# =================  Operator Precedence ========================== #
print( not 0)  # True
print( not 1)  # False
print(0 and 1)   # 0
print( 1 and 20)   # 20
print({} and [])   # {}
print({} or 6)    # 6

# print({} and 6)   # {}
# print({} or 6)    # 6
# print(6 and {})   # {}
# print(6 or {})    # 6
#
# print(6 and 7)   # 7
# print(6 or 7)     # 6
#
#
r = 13 and {} and 5  or [] and 6  # {} and 5 or [] and 6 -> {} or [] and 6 -> {} or [] -> []
print(r)
r = 22 and [] or 32 and 0 or 67  # [] or 32 and 0 or 67 -> [] or 0 or 67  -> 0 or 67 -> 67
print(r)





