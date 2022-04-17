arr = [1,2,3,4]

# x = int(input())
# val = int(input())

# arr[x]=val
# print(arr)

def XOR(arr):
    arr_xor = 0
    for i in range(len(arr)):
        arr_xor = arr_xor ^ arr[i]
    return arr_xor


subarr = []
for i in range(len(arr)+1):    
    for j in range(i+2,len(arr)+1):
        sub = arr[i:j]
        # print(sub)
        subarr.append(sub)
print(subarr)

xor_subarr = []
for l in subarr:
    print(l)
    print(XOR(l))
    xor_subarr.append(XOR(l))
print(xor_subarr)

        
# subarr_XOR = []
# for l in subarr:
#     print(l)
#     l_xor = XOR(l)
#     subarr_XOR.append(l_xor)
    


print("final result",XOR(xor_subarr))

    