a = 10
b = a
b = 3
c = b + a

print(a, b, c)  # 10 3 22

# python is a dynamically typed language
# dynamic typing means that the type of a variable is not known until runtime
# dynamic typing is a feature of python
# that means variables are just references to memory locations they don't have
#      any type information associated with them

cgpa = 3.69  # float
is_registered = True  # boolean
is_logined = False  # boolean
country = "Bangladesh"  # string
zip_code = 1260  # integer

print(cgpa, is_registered, is_logined, country,
      zip_code)  # 3.69 True False Bangladesh 1260

# python will throw error if we using a variable that is not assigned
# print (i_am_not_assigned)

i_am_a_special_value = None
print(i_am_a_special_value)  # None
# None is a special value that represents the absence of a value in python
