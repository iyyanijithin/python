#tuple and list do the same thing
#tuple is immutable

tuple1 = (1,2,3)

#This will not work since data is tuple and it is immuatable
#'tuple' object does not support item assignment
tuple1[1] = 'roger'

print(tuple1)