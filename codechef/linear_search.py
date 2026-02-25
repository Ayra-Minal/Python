#a given number X is present in an array of size N.
#version 1
N,X = map(int, input("enter size N and key X: ").split())
flag=0
print("enter array of size N with space:")
m = list(map(int, input().split()))
for i in m:
    if i==X:
        flag=1
        break 
if flag==1:
    print("YES")           
else:
    print("NO")

'''
#version2
N, X = map(int, input().split())
A = list(map(int, input().split()))

if X in A:
    print("YES")
else:
    print("NO")
    '''