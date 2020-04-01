#Refer this as file2
#Refer this page
#https://www.journaldev.com/14036/python-data-types

#Number data type is
# int float and complex
val1 = 10
val2 = 20.0
val3 = 40

print(type(val1),type(val2), type(val3))

#You cannot concat str and type
#We can use concat with the same datatype

print(val1  + val2)
print('hello' + ' world!@!!')


#Now let us learn colleciton data type
#List will always start  with [] brackets
list1 = [1,2,3,4,5]
print(list1)
print(list1[0])
#This will refer to last index
print(list1[-1])

print(list1[1:3])

#INSERT IN A LIST
list1.insert(3, "roger")
print(list1)


#to add to the end
list1.append('rafa')
print(list1)

#To update a value at an index
list1[2] = 'rahul'
print(list1)


#Delet the value from the list
del list1[0]
print(list1)
print(list1[0])

