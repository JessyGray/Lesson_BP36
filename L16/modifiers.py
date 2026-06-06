#public
# class User:
#     def __init__(self,name):
#         self.name = name
#
# u1 = User("user")
# print(u1.name)
#protected
# class User:
#     def __init__(self,name):
#         self._name = name
#
# u1 = User("user")
# print(u1._name)
#private
class User:
    def __init__(self,name):
        self.__name = name

u1 = User("user")
# print(u1.__name)
# print(u1._User__name)