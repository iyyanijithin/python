#self is manditory for calling instance varaibles
#contructor name __init__(self)
#new keyword is not required when define obj

class Calculator:

    num = 100 #class variable / static variables

    #lets see how we define constructor

    #Default constructor
    #Constructor name is always  __init__
    #is contrctor over loading not supported ?
    def __init__(self, a, b):
        print('Default constructor')
        self.a = a
        self.b = b
        #this how we define instance variables

    #def __init__(self):
    #    print('this is default constructor')

    # Member function/ method
    def show(self):
        print('hello world')

    def sum(self):
        print(Calculator.num)
        return self.a + self.b


print('we just defined the class above')
#There is no new operation, just call the  class name
calc = Calculator(3, 4)
calc.show()
print(calc.num)
calc.num = 50
print(calc.sum())

calc = Calculator(5, 6)
calc.show()
print(calc.num)
print(calc.sum())


class Test:
    def __init__(self,a):
        self.a = a;
