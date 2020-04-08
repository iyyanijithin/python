def cal(num,value=2):
    return num ** value


method1 = lambda num,value=2: num ** value

print(cal(2, 2))
print(method1(2, 3))
