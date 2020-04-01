#In this we will do exception handling

count = 3
if count ==3:
    #raise Exception('Product count did not match')
    pass


#assert(count == 2)

try:
    with open('data23.txt', 'r') as reader:
        reader.read()
except Exception as e:
    print(e)
    print('there is an exception')
finally:
    print('finally in finally block')