# def multiply(A, B):
#     res = []

#     for i in range(3):
#         row = []
#         for j in range(3):
#             s = 0
#             for k in range(3):
#                 s = s + A[i][k] * B[k][j]
#             row.append(s)
#             print() 
#         res.append(row)
#     return res


# A = [[1,2,3],[4,5,6],[7,8,9]]
# B = [[1,2,3],[4,5,6],[7,8,9]]

# print(multiply(A, B))
# for i in m:
#     for j in i:
#         print(j,emnd="")
#     print()
# for i in range(3):
#     row=[]
#     for j in range(3):
#         s=0
#         for k in range(3):
#             s+=a[i][k]*b[k][j]
#         row.append(s)
# #     res.append(row)
# x = eval(input())

# if type(x) == list:
#     print("List")
# elif type(x) == tuple:
#     print("Tuple")
# elif type(x) == set:
#     print("Set")
# else:
#     print("Other")

# x = eval(input())

# if isinstance(x, list):
#     print("List")
# elif isinstance(x, tuple):
#     print("Tuple")
# elif isinstance(x, set):
#     print("Set")
# else:
#     print("Other")
# from functools import reduce

# l = [1,2,3,4,5]

# m = list(map(lambda x: x*x, l))
# print(m)

# r = reduce(lambda x,y: x+y, l)
# print(r)
