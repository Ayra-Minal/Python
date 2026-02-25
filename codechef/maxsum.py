#find the maximum possible 
#sum of two distinct elements in an array
#version 1
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    m=0
    for i in range (n):
        for j in range(i + 1, n):
            if a[i]!=a[j]:
                m = max(m, a[i] + a[j])
    print (m)
#take o(n^2)

#in case of any number..have or had no distinct number...ie  5 4 1 or  5 5 5 or  5 5 1
t = int(input())
while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    max1=max2=-1
    for x in a:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2=x
    if max2 == -1:#no distinct number
        temp=-1
        for x in a:
            if x<max1 and x>temp:
                temp=x
        if temp==-1:
            a.sort()
            max2=a[-2]
        else:
            max2=temp    
    print(max1 + max2)    
 
#if mentioned 2 distinct is guarenteed 
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    t -= 1
    max1=max2=-1
    for x in a:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2 and x != max1:
            max2=x
    print (max1+max2)       
#o(n)     