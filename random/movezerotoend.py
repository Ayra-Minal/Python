#Given n integers, move all zero elements to the end while maintaining the relative order of non-zero elements.

n=int(input("Enter number of elements: "))
j=0
L=[0 for i in range(n)]
for i in range(n):
    a=int(input("Enter element: "))
    if a!=0:
        L[j]=a
        print("j=",j)
        j+=1
for i in L:
    print(i,end=" ")

#or

arr = [int(input()) for _ in range(n)]

j = 0
for i in range(n):
    if arr[i] != 0:
        arr[j], arr[i] = arr[i], arr[j]
        j += 1

print(arr)    