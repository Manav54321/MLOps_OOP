# lst = [1,2,3]
# my_str = "MLOps is cool"
# my_int = 10

# print(type(lst))
# print(type(my_str))
# print(type(my_int))

# lst.clear()
# print(lst)

# my_str = my_str.upper()
# print(my_str)

from oops_proj import chatbook

user1 = chatbook()
print(user1.get_id())
user1.set_id(100)
print(user1.get_id())





# getter and setter methods
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

# function vs method:
# lst = [1,2,3]

# # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
# user1.sendmsg()