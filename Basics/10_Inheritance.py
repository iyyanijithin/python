class Calculator:

    def __init__(self, a, b):
        print('simple constructor')
        self.a = a;
        self.b = b;


    def sum(self):
        return self.a + self.b


#This is how we extend the class
class Child(Calculator):

    num3 = 100;




print('main script start here')
calc = Child(3, 4)
#We can call methods form parent
print(calc.sum())
