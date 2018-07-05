""" This module is for practicing variables """

# Variables declaration & initialization
emp_id = 1234
EMP_ID = 1234
salary = 20334.34
emp_name = "XYZ"

print(emp_id, salary, emp_name)

# # Unsupported
# db_name =
#
# Three variables assigned to same value
a = b = c = 1
print(a)
print(b)
print(c)

print(id(a), id(b), id(c))
#
# Three variables to different data
a, b, c = 1, 20.23, "python"
print(a)
print(b)
print(c)
print(id(a), id(b), id(c))
#
# Multiple statements in Single Line but not recommended by PEP8
a = 1; b = 3; c = 3456; print(a, b, c)










