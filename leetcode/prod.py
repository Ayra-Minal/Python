#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all elements except nums[i].
#Solve it without using division and in O(n) time.


arr=[2,5,6,4]
n=len(arr)
res=[1]*n

prefix=1
for i in range(n):
    res[i]=prefix
    prefix*=arr[i]

suffix=1
for i in range(n-1,-1,-1):
    res[i]*=suffix    
    suffix*=arr[i]

print(res)    