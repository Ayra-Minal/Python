# Python code reads multiple test cases and, for each test case, 
# counts how many elements in the array are not
# equal to the minimum value in the array.

t = int(input())

while t > 0:
    n = int(input("enter total"))
    a = list(map(int, input("enter array1").split()))
    t -= 1
    x=min(a)
    c=0
    for i in range (n):
        if a[i]!=x:
            c+=1
           
    print(c)

#output
#Array = [1, 2, 3, 1, 4]
#Min value = 1
#Not equal to 1: 2, 3, 4 → count = 3