#Python Built-in Functions 

#abs() function
#bin() function
#id() function
#map() function
#zip() function
#filter() function
#reduce() function
#sorted() function
#enumerate() function
#reversed() function
#range() function
#sum() function
#max() function
#min() function
#eval() function
#len() function
#ord() function
#chr() function
#any() function
#all() function
#globals() function
#locals() function


# abs
abs(-45) #45
abs(-3.14)  # 3.14
abs(10) #10
abs(2+4j) # 4.47213595499958

#Python bin() function
bin(4) # 0b100
bin(0xff) #'0b11111111'
bin(0o24) #'0b10100'

#Python id() function
a=10
b=5
id(a), id(b) # (10919712, 10919552)
a = b # a now references same object as b
id(a), id(b) #(10919552, 10919552)

#Python map() function
print(list(map(ord, ['a', 'b', 'c', 'd']))) #[97, 98, 99, 100]

##
def twice(x):
	return x*2

list(map(twice,[11,22,33,44,55])) # [22, 44, 66, 88, 110]

##
def calc_sum(x1, x2):
	 return x1+x2


list(map(calc_sum, [1, 2, 3, 4, 5], [10, 20, 30])) ## [11, 22, 33] olanları toplar

## 
def foo(x1,x2):
	if x2 in None:
		return x1
	else:
		return x1+x2


list(map(foo, [1, 2, 3, 4, 5], [10, 20, 30])) ## [11, 22, 33, 4, 5] olmayanlar(indexi yetmeyenler) aynen döner 

#Python zip() function
list(zip([1, 2, 3, 4], "pow")) #[(1, 'p'), (2, 'o'), (3, 'w')]

#
for i, j, k, l in zip([1, 2, 3], "foo", ("one", "two", "three"), {"alpha", "beta", "gamma"}):
	print(i, j, k, l)
	#1 f one alpha
	#2 o two gamma
	#3 o three beta
##
keys = ['alpha', 'beta', 'gamma']
values = [10, 20, 30]
d = dict(zip(keys, values))  #{'alpha': 10, 'beta': 20, 'gamma': 30}

# Python filter() function
def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


f = filter(is_even, [1, 3, 10, 45, 6, 50])
print(*f) # 10,6,50

#Python reduce() function
from functools import reduce
def do_sum(x1, x2): return x1 + x2
reduce(do_sum, [1, 2, 3, 4])

#
def my_reduce(func, seq):
	first = seq[0]
	for i in seq[1:]:
		first = func(first, i)
	return first

def do_sum(x1, x2):
	return x1 + x2

print(my_reduce(do_sum, [1, 2, 3, 4])) ## my_reduce fonksiyon yazımı

#Python sorted() function
ages = [45, 11, 30, 20, 55]
sorted(ages) # [11, 20, 30, 45, 55]
sorted(ages, reverse=True) #[55, 45, 30, 20, 11]

#
fruits=['lime', 'blueberry', 'plum', 'avocado']
sorted(fruits, key=len) # ['lime', 'plum', 'avocado', 'blueberry'] sort by string length 

#
 t = ( 'AA', 'aa', 'ZZ', 'cc', 'bb')
 sorted(t) #['AA', 'ZZ', 'aa', 'bb', 'cc']
 sorted(t, key=str.lower) # ['AA', 'aa', 'bb', 'cc', 'ZZ']
class Employee:
     def __init__(self, name, salary, age):
         self.name = name
         self.salary = salary
         self.age = age
 
     def __repr__(self):
         return self.__str__()
 
     def __str__(self):
         return "{0}:{1}:{2}".format(self.name, self.salary, self.age)
 
 
 
 e1 = Employee("Tom", 20000, 32)
 e2 = Employee("Jane", 50000, 36)
 e3 = Employee("Bob", 45000, 40)
 
 
 emp_list = [e2, e3, e1]
 
 print(emp_list) #[Jane:50000:36, Bob:45000:40, Tom:20000:32]
sorted(emp_list, key=lambda x: x.name) # sort Employee objects by name #[Bob:45000:40, Jane:50000:36, Tom:20000:32]
sorted(emp_list, key=lambda x: x.age) # sort Employee objects by age #[Tom:20000:32, Jane:50000:36, Bob:45000:40]
print(sorted(emp_list, key=lambda x: x.salary))  #[Tom:20000:32, Bob:45000:40, Jane:50000:36]

#Python enumerate() function
list(enumerate("hello")) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o')]
for index, value in enumerate("hello"):
	print(index, value)
	#0 h
	#1 e
	#2 l
	#3 l
	#4 o

for index, value in enumerate([110, 45, 12, 891, "one"]):
	print(index,value)

	#0 110
	#1 45
	#2 12
	#3 891
	#4 one
for index, value in enumerate({'name': 'Jane', 'age': 26, 'salary': 40000}):
	print(index,value)
	#0 name
	#1 salary
	#2 age

#
list(enumerate("hello", start=2)) #[(2, 'h'), (3, 'e'), (4, 'l'), (5, 'l'), (6, 'o')]

#Python reversed() function
list(reversed([44, 11, -90, 55, 3])) #[3, 55, -90, 11, 44]
list(reversed((6, 1, 3, 9))) # reversing a tuple  [9, 3, 1, 6]

#Python range() function
list(range(5)) # 0,1,2,3,4
list(range(-100, -95)) # [-100, -99, -98, -97, -96]

#Python sum() function
sum([1, 2, 3, 4, 5]) # sum values in a list #15
sum([10, 20, 30], 100)# 160

#Python max() function
 max("abcDEF") # c
 max([2, 1, 4, 3]) # find largest item in the list #4,
 max([], default=0) # supressing the error with default value #0

#Python min() function
min("abcDEF") # find smallest item in the string  #D
min([2, -1, 4, 3]) # find smallest item in the list # -1
min([], default=0) # supressing the error with default value #0

#Python ord() function
ord("A") #65
ord("f") # 102
#Python chr() function
chr(65)  # A
chr(128512) # Grinning Face #:)

#Python any() function
any([10, "", "one"]) # True
any(("", {})) #False

#Python all() function
all(['alpha', 'beta', '']) #False
all(['one', 'two', 'three']) #True
all([]) #True