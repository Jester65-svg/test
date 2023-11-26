'''
arr=[9089, -67, -32, 1, 20, 23, -65, 99, 9089, 34, 20, 0, -67, 1, 11, 111, 111, 1, 23]
len(arr)
for k in range (1):
    for i in range (len(arr)):
        if arr[i]==20:
            arr[i]=200
print(arr)
'''
arr=[9089, -67, -32, 1, 20, 23, -65, 99, 9089, 34, 20, 0, -67, 1, 11, 111, 111, 1, 23]
b=arr.index(20)
arr[b]=200
print(arr)
