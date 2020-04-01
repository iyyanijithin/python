#This sample will show how do to file handling
file = open('data.txt')
#print(file.read())
print('using file again')
print(file.read(3))
print(file.readline())
print(file.readline())
#There is a file pointer which keeps moving
print(file.readline())
print(file.readline())
file.close()


file = open('data.txt')
for line in file.readlines():
    print(line)
file.close()

#Better syntax which will close the file automatailly
with open('data1.txt', 'w') as file:
    file.write('writing data')

#DO an excercise to read file content and erver it