
t = int(input("test case: "))

while t > 0:
    n = int(input("number of elements: "))
    d = list(map(int, input("enter").split()))
    t -= 1
    if d == sorted(d):
        print(d)
        print ("yes")
    else:
        print("no")

