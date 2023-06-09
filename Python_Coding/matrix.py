import numpy as np
my_list = [[3,5,22,66], [4,3,77,22], [4,4,6,67], [42,4,6,67]]
my_array = np.array(my_list)
print(my_array)
print(type(my_array))

my_matrix = np.reshape(my_array,(4,4))
print(my_matrix)
print(type(my_matrix))

print(my_matrix[1])
print(my_matrix[1,0])

one_list = [[1,2,3,3,6,2,6,4,2], [3,9,4,5,5,7,3,2,1], [8,9,0,9,8,0,7,4,4]]
print(one_list)
a = np.array(one_list)
print(a)

x = np.reshape(a,(3,9))
print(x)
print(type(x))
print(type(a))
