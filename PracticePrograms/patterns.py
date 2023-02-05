# # # patterns with loops

# # for i in range(4):
# #     for j in range(4):
# #         print("# ",end="")
# #     print()

# # print("\nTriangle Shape\n")
# # for i in range(4):
# #     for j in range(i+1):
# #         print("# ",end="")
# #     print()

# # print("\nInverted Triangle\n")
# # for i in range(4):
# #     for j in range(4-i):
# #         print("# ",end="")
# #     print()

# # # diamond
# # # symmetric triangle
# # # inverted symmetric triangle


# for i in range(5):
#     for j in range(i+1):
#         print("*", end="")
#     print()
    
# print("Inverted Pattern")
# for i in range(6):
#     for j in range(6-i):
#         print("*",end="")
#     print()

# print("right angled triangle")
# for i in range(6):
#     for j in range(6-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()

# print("Inverted right angled triangle")
# for i in range(6):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(6-i):
#         print("*",end="")
#     print()
    
# print("Triangle")
# for i in range(6):
#     for j in range(6-i):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()

# print("inverted triangle")
# n = int(input())
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(n-i):
#         print("* ",end="")
#     print()

# print("Diamond")
# for i in range

# for i in range(5):
#     for j in range(5):
#         if(j>i):
#             print(j,end="")
#         else:
#             print(i,end="")
#     print()

# print("Diamond")
# n = int(input())
# r = n//2 + 1
# for i in range(r+1):
#     for j in range(r-i):
#         print(" ",end="")
#     for j in range(i):
#         print("* ",end="")
#     print()

# for i in range(1,r):
#     for j in range(i):
#         print(" ",end="")
#     for j in range(r-i):
#         print("* ",end="")
#     print()

from math import factorial


for i in range(7):
    for j in range(7-i):
        print("  ",end="")
    for j in range(i+1):
        print(int(factorial(i)/(factorial(i-j)*factorial(j))),end="  ")
    print()