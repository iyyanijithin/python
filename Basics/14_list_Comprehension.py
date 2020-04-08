string = 'php'
print(type(string))
#Example of string comprehension
len_lc = [string.count(elem) for elem in string]
print(len_lc)

len_dc = {elem:string.count(elem) for elem in string}
print(len_dc)