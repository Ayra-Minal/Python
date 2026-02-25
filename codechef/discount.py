#shopping for fruits, and you have the option to buy a discount coupon.
#The coupon costs x units, and it reduces the price of each fruit by y units (but not below 0).
#You want to decide whether it's worth buying the coupon or not.
#n → number of fruits
#x → cost of the coupon
#y → discount per fruit ,r is 0 if negative
#a the prices of the fruits.
#fb=final price before
#t = testcase
t = int(input())
while t > 0:
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    t -= 1
    fb=sum(a)
    na=[]
    for m in a:
        r=m-y
        if r < 0:
            na.append(0)
        else:
            na.append(r)
    fa=(sum(na)+x)
    if fa<fb:
        print("COUPON")
    else:
        print("NO COUPON")

'''
INPUT=
2
3 10 5
10 5 2
4 15 3
6 2 5 8

OUTPUT=
COUPON
NO COUPON
'''