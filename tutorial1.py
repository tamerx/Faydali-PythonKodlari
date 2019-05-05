############ python variables ##################
x = "Python is "
y = "awesome"
z =  x + y
print(z)
##############
x = 5
y = 10
print(x + y)
#############
x = 5
y = "John"
print(x + y) ## giving error

########### Pyton Numbers ################

x = 1    # int
y = 2.8  # float
z = 1j   # complex
#######
x = 1
y = 35656222554887711
z = -3255522

print(type(x)) #int
print(type(y)) #int
print(type(z)) #int

#######################
x = 1.10
y = 1.0
z = -35.59

print(type(x)) ## float
print(type(y)) ## float
print(type(z)) ## float

######################
x = 35e3
y = 12E4
z = -87.7e100

print(type(x)) ## float
print(type(y)) ## float
print(type(z)) ## float
#######################
x = 3+5j
y = 5j
z = -5j

print(type(x)) ## complex
print(type(y)) ## complex
print(type(z)) ## complex
######### Python Casting ##############
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
#################
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
#################
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

##################### Python Strings #########################
a = "Hello, World!"
print(a[1])
###################
b = "Hello, World!"
print(b[2:5])
###################
## başta ve sondaki boşlukları siler
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
##################
a = "Hello, World!"
print(len(a))
##################
#### H yerine J yazar
a = "Hello, World!"
print(a.replace("H", "J"))

########################
## virgüle göre böler ve list dönderir
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

########################## Python Operators ####################
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

##################

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)

# returns False because z is the same object as x

print(x is not y)

# returns True because x is not the same object as y, even if they have the same content

print(x!= y)

# to demonstrate the difference betweeen "is not" and "<>": this comparison returns False because x is equal to y


########################## Python Lists ##########################
thislist = ["apple", "banana", "cherry"]
print(thislist)
###################
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

###################
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
############## Python List append() Method 
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
#############
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b) ### a = ['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]
############## Python List clear() Method
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
############## Python List copy() Method 
fruits = ['apple', 'banana', 'cherry', 'orange'] 
x = fruits.copy() ### Not: fruits 'de  yapılan daha sonraki değişiklik x 'e yansımaz copy metodundan ötürü.
############
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)

################## Python List extend() Method 
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars) ## list gibi değil yeni elemanlar gibi davranır
##########
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
################### Python List index() Method 
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
################### Python List insert() Method
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
#################### Python List pop() Method
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1) ## elemanı siler

#################### Python List remove() Method
fruits = ['apple', 'banana', 'cherry'] 
fruits.remove("banana") ## eğer eleman listede yoksa hata verir

################### Python List reverse() Method 
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()

################# Python List sort() Method 
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
#############
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
##################
## alternatif lambda
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key= lambda x:len(x))
print(cars)


############################## Python Tuples #########################
thistuple = ("apple", "banana", "cherry")
print(thistuple)
###############
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
##################
thistuple = ("apple", "banana", "cherry")
thistuple[1] = "blackcurrant" # değiştirilemez hata verir
# The values will remain the same:
print(thistuple)
##################
#Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists

########## Python Tuple count() Method 
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)
######## Python Tuple index() Method 
## ilk 8 olan değerin indeksini dönderir
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)

######################## Python Sets #######################################
thisset = {"apple", "banana", "cherry"}
print(thisset)
########
## add items
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
#### add multiple items
thisset = {"apple", "banana", "cherry"}
thisset.update(["orange", "mango", "grapes"])
print(thisset)
###### remove item
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") ## eğer banana elemanı yoksa hata verir.
print(thisset)
####### remove item (discard)
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") ## banana elemanı yoksa hata vermez.
print(thisset)
######## clear set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
#############
#The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
#################
#Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
######### Python Set add() Method
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
######## Python Set clear() Method
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
###########  Python Set copy() Method
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
########## Python Set difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
print(z) # {"cherry","banana"}
########## Python Set difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) 
print(x) ## her iki kümede olanı siler, tekrarlanmayanları yazdırırı  # {"cherry","banana"}
######### Python Set discard() Method
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana") 
print(fruits)  ### banana elementini siler
########## Python Set intersection() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y) 
print(z) ## kesişen elemanı alır
##### 
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result) ## c değeri döner
############## Python Set intersection_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y) 
print(x) ### kesişeni yazdırır, ortak olmayanları siler
#######
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)
################### Python Set isdisjoint() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)  ## ortak elemanları yoksa True,varsa False (Bu iki küme farklı mı)
print(z)
######
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y) 
print(z)
################## Python Set issubset() Method
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)  ## x , y'nin alt kümesi mi
print(z) #True
#########
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b"}
z = x.issubset(y) 
print(z) #False
################### Python Set issuperset() Method
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) ## x , y'yi kapsar mı 
print(z)  # True
########
x = {"f", "e", "d", "c", "b"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
print(z) # False
################# Python Set pop() Method
#Remove a random item from the set:
fruits = {"apple", "banana", "cherry"}
fruits.pop() 
print(fruits)
################# Python Set remove() Method
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana") 
print(fruits)
################ Python Set symmetric_difference() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) #kesişmeyenleri alır ,fark alır
print(z) #{'google', 'microsoft', 'banana', 'cherry'}
################ Python Set symmetric_difference_update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) #kesişmeyenleri alır , diğerlerini siler
print(x)
##############  Python Set union() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.union(y) ## birleşimini alır
print(z)## {'banana', 'apple', 'microsoft', 'cherry', 'google'}
############ Python Set update() Method
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y) 
print(x)
######################## Python Dictionaries #######################################
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#### Accessing Items
x = thisdict["model"]
x = thisdict.get("model")
#### Change Value
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
##### Loop Through a Dictionary
## key dönderir
for x in thisdict:
  print(x)
## value dönderir
for x in thisdict:
  print(thisdict[x])

for x in thisdict.values():
  print(x)

### değerleri dönderir
for x, y in thisdict.items():
  print(x, y)
### Add item
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
##### Removing Items
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
## popitem() son elemanı siler
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
## del metodu
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# The del keyword can also delete the dictionary completely:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
### Clear
#The clear() keyword empties the dictionary:

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
### The dict() Constructor

thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
print(thisdict)
############# Python Dictionary clear() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()

print(car)
############# Python Dictionary copy() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.copy() ### car verisinde değişiklik x 'i  etkilemez.

print(x)
############## Python Dictionary fromkeys() Method
## varsayılan 0 olarak bir dictionary oluşturur
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)
## varsayılan None olarak bir dictionary oluşturur
x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

################### Python Dictionary get() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("model")
print(x)
#### olmaynan değeri varsayılan olarak çeker , None dönebilir
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.get("price", 15000)
print(x)
################# Python Dictionary items() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()

print(x) ## dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

#### atama gibi değişiklik her nesnede olur
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.items()
car["year"] = 2018
print(x) ### dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2018)])

######################## Python Dictionary keys() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.keys()
print(x) ## dict_keys(['brand', 'model', 'year'])


#### atama gibi değişiklik her nesnede olur
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.keys()
car["color"] = "white"
print(x)  ### dict_keys(['brand', 'model', 'year', 'color'])

#################### Python Dictionary pop() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car) ### model silinir {'brand': 'Ford', 'year': 1964}

#### çektiği değeri verir
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.pop("model")
print(x) ## mustang
print(car) ### {'brand': 'Ford', 'year': 1964}
################ Python Dictionary popitem() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.popitem() ## son elemanı siler
print(car)  ## {'brand': 'Ford', 'model': 'Mustang'}


## en son değeri siler , tuple olarak dönderir
#The removed item is the return value of the pop() method:

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.popitem()
print(x)

####################### Python Dictionary setdefault() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("model", "Bronco") ## eğer model değeri olmasaydı varsayılan olarak verilirdi
print(x)
######
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("color", "white")

print(x)
########### Python Dictionary update() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.update({"color": "White"})
print(car)
######################## Python Dictionary values() Method
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
print(x)

### değişiklik olur
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.values()
car["year"] = 2018
print(x)

########################################### Python Lambda ########################################
x = lambda a : a + 10
print(x(5))
####
x = lambda a, b : a * b
print(x(5, 6))
##################
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

###################
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

################# Python Try Except #########################################
#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
#The finally block lets you execute code, regardless of the result of the try- and except blocks.
######
try:
  print(x)
except:
  print("An exception occurred")
#######
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
######
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
######
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
########
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
############################ File Handling ######################################
######### Python File Open
#"r" - Read - Default value. Opens a file for reading, error if the file does not exist

#"a" - Append - Opens a file for appending, creates the file if it does not exist

#"w" - Write - Opens a file for writing, creates the file if it does not exist

#"x" - Create - Creates the specified file, returns an error if the file exists

f = open("demofile.txt")
#The code above is the same as:
f = open("demofile.txt", "rt")
######### Python Read File
f = open("demofile.txt", "r")
print(f.read())
######
#Read one line of the file:

f = open("demofile.txt", "r")
print(f.readline())
####### Python File Write
#Open the file "demofile.txt" and append content to the file:
f = open("demofile.txt", "a")
f.write("Now the file has one more line!")
#####
#Open the file "demofile.txt" and overwrite the content:
f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")

###### Create a New File
#To create a new file in Python, use the open() method, with one of the following parameters:

#"x" - Create - will create a file, returns an error if the file exist

#"a" - Append - will create a file if the specified file does not exist

#"w" - Write - will create a file if the specified file does not exist

f = open("myfile.txt", "x") ## varsa hata verir , yoksa oluşturur
f = open("myfile.txt", "w") ## varsa yada yoksa yeniden oluşturur

######## Delete a File
import os
os.remove("demofile.txt")

######  Check if file exist, then delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

####  How to Remove Duplicates From a Python List
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)
### How to Reverse a String in Python
txt = "Hello World"[::-1]
print(txt)