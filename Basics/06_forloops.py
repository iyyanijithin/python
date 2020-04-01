#In this file we will learning looping in python

dataList = [1,2,3,4]

#loop over all the objects
for data in dataList:
    print(data)

print('to Iterate over a range')
#interate over a range
sumVal = 0
for j in range(1, 6):
    sumVal = sumVal + j
print(sumVal)

#In case for  range we want incr by 2
#to loop until 9 with incr
for k in range(1, 10, 2): #start with 1 and move till 5 (6-1) Default counter is 1
    print(k)

#To loop 10 times
count = 10
for m in range(count):
    print(m)

