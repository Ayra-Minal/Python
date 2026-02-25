#It calculates the total cost of items that are "fresh enough" 
#(i.e., their freshness is
#greater than or equal to a given threshold x).

t = int(input())

while t > 0:
    n, x = map(int, input().split())
    f = list(map(int, input().split()))
    c = list(map(int, input().split()))
    t -= 1
    fi=[]
    for i in range(len(f)):
        if f[i] >= x:
            fi.append(i)
    cost=0
    for i in fi:
        cost+=c[i]
    print(cost)            
            