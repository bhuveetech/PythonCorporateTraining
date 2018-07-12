"""To practise functions"""


def fun_example1(arg1, arg2):
    """Sample functions """
    print(arg1, arg2)


# fun_example1(20, 30)   # 2 positional
# fun_example1(20, arg2=30)  # 1 positional and 1 keyword argment
# fun_example1(arg1=20, arg2=30)  # 2 Keyword/ name arguments
# fun_example1(arg2=20, arg1=30)   # 2 keyword


def fun_example2(arg1, arg2, default_arg1=20):
    """Sample functions """
    print(arg1, arg2, default_arg1)


# fun_example2(20, 30)    # 2 positional argument
# # #fun_example(20)
# fun_example2(30, 30, 70)  # arg1= 30 arg2=30 default_arg1=70
# fun_example2(30, arg2=80 , default_arg1=80)   # 1 Positional argument and 2 keyword argument
# # arg1=30 arg2=80 default_arg1=80
# #fun_example2(arg2=40, 70, 80)  # No Support of positional args followed by keyword argument
# fun_example2(70,80, default_arg1=40)  # arg1=70 arg2=80 default_arg1=40


def fun_example3(arg1, arg2, default_arg1=20, *args):
    """Sample functions """
    print(arg1, arg2, default_arg1, args)   # 20, 30, 20
    #return

# fun_example3(20, 30)    # 2 positional argument   # 20, 30, 20
# fun_example3(20, 30, 40)   # 20, 30 , 40
# fun_example3(20, 30, 40, 50, 60, 70)   #
# print(fun_example3(20, 30))   # True


def fun_example4(arg1, arg2, default_arg1=20, *args, **kwargs):  # Packing
    """Sample functions """
    print(arg1, arg2, default_arg1, args, kwargs)


# fun_example4(arg1=20, arg2=40, default_arg1=70)  # 3 keywords , 0 positional argument
# fun_example4(arg1=20, arg2=40, default_arg1=70, name='xyz')   # 4 keyword
# fun_example4(20, 30, 40, 70, 80, 90, name='yz', name2='zx')  # 20, 30, 40 , (70,80,90)

# fun_example4(*(20, 30, 40), 70, 80, 90, **{"name":'yz', "name2":'zx'})  # Unpack
# fun_example4(20,30,40,70,80,90,name='yz',name2='zx')
#
# list_values1 = (20,30,40)
# key_values ={"name":'yz',"name2":'zx'}
#
# fun_example4(*list_values1, 70,80,90, **key_values)


def fun_example(arg1, default_arg1=20, *args, keyword_arg, **kwargs):
    """Sample functions """
    print(arg1, default_arg1, args, keyword_arg, kwargs)


# fun_example(20, 30, 40, 50 , 60, 70, keyword1_arg=60, keyword_arg=40, name="python")    # 1 positional argument, 1 keyword argument
# # arg1= 20 default_arg1=30 args=(40,50,60,70) keyword_arg=40 {"keyword1":60, "name':"python"}



# #fun_example(20)
# fun_example(30, 70, keyword_arg=80)
# fun_example(arg1=40, default_arg1=80, keyword_arg=70)
# fun_example(keyword_arg=80, default_arg1=80, arg1=40)


def func_example(arg1, list_arg):
    """Example for call by reference"""
    print(id(list_arg))
    list_arg.append(30)
    print(list_arg)   # [1,2, 3, 4, 30]


# list1 = [1, 2, 3, 4]
# print(list1)      # [1, 2, 3, 4]
# print(id(list1))
# func_example(20, list1)   #2 position argument arg1= 20  list1_arg = list1
# print(list1)  # [1,2, 3, 4, 30]


def func(arg, arg2=[]):
    """Mutable data as default value"""
    arg2.append(arg)
    print(arg2)      # [1,2,3]


# func(arg=1) # arg=1 arg2 = []  [].append(1) -> [1]
# func(arg=2)  # arg=2  [1].append(2) -> [1, 2]
# func(arg=3)


def func(arg, arg2=None):
    """Mutable data as default value"""
    if arg2 is None:
        arg2 = []
    arg2.append(arg)
    print(arg2)      # [1]

# func(arg=1)  # arg=1 arg2=None arg2 = [] [].append(1) -> [1]
# func(arg=2)  # arg=2  None  arg2 = [] [].append(2) -> [2]


var = 1                 # Global
# print(var)  # 1


def outer_func():
    var = 20
    print(var)  # 20

    def inner_func():
        var = 40  # Local
        print(var)  # 40

    inner_func()
    return 1


# print(var)   # 1
# outer_func()
# print(var)   # 40

#
#

var = 1


def outer_func2():
    global var   # Point to Global variable 'var'
    var = 20   # 20

    def inner():
        global var  # Point to Global Variable 'var'
        var = 40   # 40
        print(var)

    inner()

# print(var)   # 1
# outer_func2()
# print(var)   # 40


arg2 = 1   # Global variable arg2


def outer_func3():
    arg2 = 20    # Create local variable "arg2"

    def inner():
        nonlocal arg2   # Point to parent functions' variable "arg2"
        arg2 = 40
        print(arg2)   # 40

    print(arg2)  # 20
    inner()
    print(arg2)   # 40


# outer_func3()
# print(arg2)   # Point to Global variable

var = 1


def outer_func4():
    global var     # Point to global variable "var"
    var += 40      # Changing Global variable
    arg2 = 20      # Creating Local Variable
    print(arg2)

    def inner():
        global var   # Point to Global variable
        nonlocal arg2  # Point to parents functions variable
        var += 60
        arg2 += 40

    inner()
    print(arg2)

# print(var)
# outer_func4()
# print(var)


var = 1


def outer_func5():
    global var     # Point to global variable "var"
    var += 40      # Changing Global variable
    arg2 = 20      # Creating Local Variable
    print(arg2)
    print(var)

    def inner():
        global var   # Point to Global variable
        nonlocal arg2  # Point to parents functions variable
        var += 60
        arg2 += 40
        print(arg2)
        print(var)

        def inner1():
            nonlocal arg2
            arg2 = 70
            print(arg2)
            print(var)

        inner1()

    inner()
    print(arg2)

print(var)
outer_func5()
print(var)




