#program to find whether number of times both 
# susan and james are happy.tested by seeing is susan ran twice than him or wise verse...
# both happy if neither condition met
t = int(input())

while t > 0:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    t -= 1
    c=0
    for i in range (n):
        if 2*a[i]<b[i] or 2*b[i]<a[i]:
            continue
        else:
            c+=1
    print(c)        