nums = [1,2,3,3,4]
target = 8

a= -1
b= -1

for num in nums:
    a+=1
    b=-1
    for num2 in nums:
        b+=1
        if num+num2 == target:
            print ("["+str(a)+"] ["+str(b)+"]")





