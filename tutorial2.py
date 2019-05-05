# iki ayrı listin tek tek elemanlarını toplar
A = [9, 8, 7, 6, 5]
B = [3, 4, 5, 6, 1]
C=[]

for x, y in zip(A, B):
	C.append(x+y)
print(C)## [12, 12, 12, 12, 6]
###### List elemanlarına belirtilen karakteri ekleme
mylist = ['butter', 'jam', 'curd']
myStr = ', '.join(mylist)
print(myStr) ## string dönderir(butter, jam, curd)
###### Listi ayrıştırıp string olarak alma
mylist = [1, 11, 111]
myStr = str(mylist).strip('[]')
print(myStr)
print(type(myStr))  #1, 11, 111
###### Boş dictonary
emptyList = {}
###### has_key() , parametre olarak verilen veriye sahip mi.
#To check if a particular key exists in the dictionary,
#this function can be used.
#If the key that you are looking for exists then it returns True, otherwise False
myDictionary.has_key("Key-2")

######## iki dict nesnesini karşılaştırma
x = {1: 1, 2:2, 3:3}
y = {1:1.0, 2:2, 3:3}
print(x==y) ## True

#### Python Tuple
secondTuple = 1, 2, "python", 4
print(secondTuple) 
#### tuple tanıtma
emptyTuple = ()
anotherEmptyTuple = tuple()
### tuple 'a eleman ekleme
t = (1, 2, 3, 4, 5)
t = t + (7,)
### iki tuple birleştirilebilir
print (1, 2, 5, 8) + (2, 9, 4) #(1, 2, 5, 8, 2, 9, 4)