class Calculator:

    def __init__(self, a, b):
        print('simple constructor')
        self.a = a;
        self.b = b;


    def sum(self):
        return self.a + self.b


class Child(Calculator):

    num3 = 100;



print('main script start here')
calc = Child(3, 4)
print(calc.sum())
