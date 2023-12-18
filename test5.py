# class A:
#     def __init__(self):
#         print("A")


# class B:
#     def __init__(self):
#         print("B")


# class C(A):
#     def __init__(self, arg):
#         print("C", "arg = ", arg)
#         A.__init__(self)


# class D(B):
#     def __init__(self, arg):
#         print("D", "arg = ", arg)
#         B.__init__(self)


# class E(C, D):
#     def __init__(self, arg):
#         print("E", "arg = ", arg)
#         C.__init__(self, arg)
#         D.__init__(self, arg)


# E(10)
# print("MRO:", [x.__name__ for x in E.__mro__])


class SuperA:
    def __init__(self):
        print("A")
        super().__init__()


class SuperB(object):
    def __init__(self):
        print("B")
        super().__init__()


class SuperC(SuperA):
    def __init__(self, arg):
        print("C", "arg = ", arg)
        super().__init__()


class SuperD(SuperB):
    def __init__(self, arg):
        print("D", "arg = ", arg)
        super().__init__()


class SuperE(SuperC, SuperD):
    def __init__(self, arg):
        print("E", "arg = ", arg)
        super().__init__(arg)


print("MRO:", [x.__name__ for x in SuperE.__mro__])
SuperE(10)
