# 1 <= x <= y <= N
# find number of pairs of (x,y) 
# so that sum([1,2..,x-1]) == sum([x+1,x+2,...y])


N = int(input())

# def findPairs(N):
#     count = 0
#     for i in range(1,N+1):
#         for j in range(i+1,N+1):
#             s1 = sum(range(1,i))
#             print(s1)
#             s2 = sum(range(i+1,j+1))
#             print(s2)
        
#         # print("i",i)
#         # for j in range(i,N+1):
#         #     print("j of i", j,i)
#         #     n1 = range(1,i-1)
#         #     print(n1)
#         #     n2 = range(i+1,j)
#         #     print(n2)
#         #     s1 = sum(n1)
#         #     print("s1",s1)
#         #     s2 = sum(n2)
#         #     print("s2",s2)
#             if s1 == s2:
#                 count = count+ 1
#             else:
#                 count = count + 0
#     return count


def findPairs(N):
    count = 0
    for x in range(1,N+1):
        for y in range(x,N+1):
            print("pair:",x,y)
            s1 = sum(range(1,x))
            print(s1)
            s2 = sum(range(x+1,y+1))
            print(s2)
            
            if s1==s2:
                count = count+1
            else:
                count = count + 0
        return count
    


result = findPairs(N)
print("Result is",result)