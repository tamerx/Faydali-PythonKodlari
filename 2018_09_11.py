
## Bu örnek ile çok karşılaşıyorum  ilk parametre(ArgCount) herhangi bir değişken olabilir
# ikinci(VarArgs) değişken tuple olarak değerlendirilir.
# ücüncü degisken(kwargs) ise dictionary olarak değerlendirilir

def Hello4(ArgCount, *VarArgs,**kwargs):
	print("You passed ", ArgCount, " arguments.")
	for Arg in VarArgs:
		print(Arg)

	for  k,v in kwargs.items():
		print(k,v)

dict={"a":2,"b":3,"c":4}
Hello4(5,1,2,3,4,dict)

############################################
try:
    Value = int(input("Type a number between 1 and 10:"))
    if (Value > 0) and (Value <= 10):
        print("You typed: ", Value)
    else:
        print("1 ile 10 arasi sayi gir")
except ValueError as e:
    print("tip yanlis")
    print(e)


++++++++++++++++++
import sys

try:
    File = open('exampleFilex.txt')
    print("File opened as expected.")
    File.close();
except IOError as e:
    print("Error opening file!\r\n" +
          "Error Number: {0}\r\n".format(e.errno) +
          "Error Text: {0}".format(e.strerror))


+++++++++++++++++++++++++++
try:
    bolunen =5
    bolen =  0
    print(bolunen/bolen)
except ZeroDivisionError:
    print("bir sayıyı 0'a bölemezsiniz")
    raise
############################################
## collections kütüphanesinden Counter kullanarak bir listenin içindeki geçen elemanlarını bulan kod parçası
## Her bir item tuple olarak dönüyor.
from collections import Counter

MyList = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 5]
ListCount = Counter(MyList)
print(ListCount)
for ThisItem in ListCount.items():
    print("Item: ", ThisItem[0], " Appears: ", ThisItem[1])
    print("The value 1 appears {0} times.".format(ListCount.get(1)))
############################################
##Bazı list operatörleri
shoplist = ['apple', 'mango', 'carrot', 'banana']

print(shoplist[::1])
print (shoplist[::2])
print (shoplist[::3])
print(shoplist[::-1]) ## reverse özelliği ile aynı ama referans olarak kopya edilmeyen işlerde kullanılabilir
##############################################
## lambda operatorunu kullanarak listi sıralama örneği
points = [ { 'x' : 2, 'y' : 3 },
{ 'x' : 4, 'y' : 1 } ]
points.sort(key=lambda i : i['y'])
print points
##################################################
## güzel bir string yazdırma örneği  buraya dikkat -> "%s=%s" % (k,v)
def buildConnectionString(params):
    return "; ".join(["%s=%s" % (k, v) for k, v in params.items()])


if __name__ == "__main__":
    myParams = {"server": "mpilgrim", \
                "database": "master", \
                "uid": "sa", \
                "pwd": "secret" \
                }
    print(buildConnectionString(myParams))

#### bu da bir başka

sent="%s is 15 years old"
name="tamer"
print(sent%name)
print(sent%("nuri"))

##################################################
## python swap operatörü ile güzel bir fibonacci serisi yazdırma

def fiv(x):
    a = 0
    b = 1
    while b < x:
        print(a)
        a, b = b, b + a
        x += 1
fiv(50)
##################################################
## split fonksiyonun çeşitli kullanım örneği
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']

s=';'.join(li)
print(s)
print(s.split(";"))
print(s.split(";",1))
print(s.split(";",2))

#################################################
## filtreleme fonkisyonu örneği
def filterx(x):
	if len(x)>1:
		return True
li=["a","mp","foo","b","c","d","e"]

li2=list(filter(filterx,li))
print(li2)
#################################################
##  değişik fonksiyon kullanma özellikleri
def add(x):
    def inner(y):
        return x + y
    return inner


inc = add(1)

print(inc(5))
print(add(1)(3))
## aynı örneği lambda kullanılarak gösterilmesi:
add =lambda x: lambda y:x+y
inc = add(1)

#################################################
##çözemediğim bir örnek:)
import re
replace = lambda patter: lambda repl: lambda string: \
    re.sub(patter, repl, string)
censor = replace(r"[aeiou]")("*")
map_ = lambda f: lambda iterable: list(map(f, iterable))
censor_all = map_(censor)
print(censor_all(["PyCon AU", "Sunday Sesh"]))

#################################################
## palindorom string kontrolü
func = lambda x:True if x==x[::-1] else False
## daha fonksiyonel
func = lambda x: x==x[::-1]
#################################################
## reduce kullanım örneği
from functools import reduce
a=[1,2,3,4]

print(reduce(lambda x,y:x*y,a))
#################################################
## bir fonksiyona *args ve **kwargs parametre olarak gönderim örneği
def test_args_kwargs(arg1,arg2,arg3):
	print("arg1",arg1)
	print("arg2",arg2)
	print("arg3",arg3)

args=("two",3,5)
kwargs={"arg3":3,"arg2":"two","arg1":5}

test_args_kwargs(*args)
print("\n")
test_args_kwargs(**kwargs)
#################################################
## yield sözcüğü kullanım örneği
def generator_function():
	for i in range(40):
		yield i


def fibon(n):
	a=b=1
	for i in range(n):
		yield a
		a,b=b,a+b

for x in fibon(20):
	print(x)
#################################################
## iki farklı fonksiyonu tek bir liste üzerine map etme örneği
def multiply(x):
    return x * x


def add(x):
    return x + x

funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)
#################################################
## bir liste içindeki elemanları reduce kullanarak toplama örneği
from functools import reduce
product = reduce((lambda x,y:x+y),[1,2,3,4])
print(product)
#################################################
## ternary kullanım örneği
fat = True
fitness = ("skinny", "fat")[fat]
print("Ali is ", fitness)
#################################################
## fonksiyon decarator kullanımı
from functools import wraps

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated

@decorator_name
def func():
    return "Function is runnig"

if __name__ == '__main__':
    can_run = False

    print(func())
# can_run=False
# print(func())
#################################################
## fonksiyon dekaratör örneği 2
def a_new_decorator(a_func):
    def wrap_the_function():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrap_the_function


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
a_function_requiring_decoration()
##################################################
## fonksiyon dekaratör kullanım örneği3
def a_new_decorator(a_func):
    def wrap_the_function():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrap_the_function


@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


a_function_requiring_decoration()
##################################################
##  collections dan defautdict kullanım örneği
from collections import defaultdict

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),)

print(type(colours))

favorite_colours = defaultdict(list)

print(type(favorite_colours))

for name, colour in colours:
    favorite_colours[name].append(colour)

for k, v in favorite_colours.items():
    print(k, v)

##################################################
## collection dan defaultdict kullanım örneği2 (çok boyutlu bir dizi gibi)
import collections
import json

tree = lambda: collections.defaultdict(tree)
some_dict = tree()
some_dict['colours']['favourite'] = "yellow"


print(json.dumps(some_dict))
#######################################################
## dict nesnesi kendi düzenine göre yazdırılıyor OrderDict kullanılarak belirlendiği gibi yazılır
from collections import OrderedDict
colours = OrderedDict([("Red", 198), ("Green", 250), ("Blue", 250)])
for key, value in colours.items():
	print(key, value)
#######################################################
## collections dan namedTuple kullanım örneği
from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print(type(Animal))
print(type(perry))
print(perry)
# Output: Animal(name='perry', age=31, type='cat')
print(perry.name)
# Output: 'perry'
#######################################################
## python enum kullanımı
from collections import namedtuple
from enum import Enum
class Species(Enum):
cat = 1
dog = 2
horse = 3
aardvark = 4
butterfly = 5
owl = 6
platypus = 7
dragon = 8
unicorn = 9
# The list goes on and on...
# But we don't really care about age, so we can use an alias.
kitten = 1
puppy = 2
#######################################################
## dictioanary nesnesinin içinde ki elemanları key e göre toplama
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3, 'B': 2}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
}
print(mcase_frequency)
#######################################################
## list içerisindeki tuple serisini 1. veya 2. elemanına göre sılama örneği
a=[(1,2),(4,1),(9,10),(13,-3)]
a.sort(key=lambda x: x[1])
print (a)
#######################################################
## çok boyutlu bir liste içindeki listeyi toplama örneği

m =[[1,2,3],[4,5,6],[7,8,9]]

l3 = [k+m+l for k,m,l in zip(*m)] # l5 daha iyi :)
l5= list(map(lambda x,y,z:x+y+z,*m))
l4= list(map(sum,m))
print(l3)
#######################################################
## zor oldu benim için :)
from functools import reduce

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 2, 3],
     [4, 5, 6], [7, 8, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9]]

print([reduce(lambda x, y: x + y, tm) for tm in list(zip(*m))])
#########################################################
## house adlı bir  objeyi price değişkenine göre sıralama örneği
def get_price(house):
	return house.price
...
>>> houses.sort(key=get_price)
########################################################
## dictionary nesnesini referansı ile kopyalama örneği
import copy

a = {'a': [1, 2, 3], 'b': [4, 5, 6]}
b = copy.deepcopy(a)
a['a'].append(4)
b['b'].append(7)
print(a)
print(b)
########################################################
## listenin içinde belirtilen koşula göre toplama örneği
print( sum(n for n in range(1, 10) if n%3==0 or n%5==0) 
########################################################
## "is" ve "==" kontrolü farklı değerler dönderiyor "is" id'ye göre bakıyor.  
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(id(x))
print(id(y))
print(id(z))

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have thew same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


#########################################################
a = ["a", "b", "c"]

x = a ## referansı ile gider
x=a.copy() ## değişikliğe tabi değil

a[0] = "31"
print(x)

#########################################################
## çok güzel bir list sıralama örneği
# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc,reverse=True)

print(cars)


########################################################
	#The difference_update() method removes the items that exist in both sets.
	#The difference_update() method is different from the difference() method, because the difference() method returns a new set, without the unwanted items, 
	#and the difference_update() method removes the unwanted items from the original set.

	##tekrarlayan veya istenmeyen silinir
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)
########################################################
## discard metodu kullanarak silme işlemi yapıldığında eleman yoksa bile hata vermez ama "remove" metodu verir
fruits = {"apple", "banana", "cherry"}

fruits.discard("banana") 

print(fruits)
########################################################
## set veri tipinde kesişim örneği
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}

result = x.intersection(y, z)

print(result)
########################################################
## tekrarlamanyan silinir
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y) 

print(x)
########################################################
##dict itemlerini liste alma örneği
a = {'x':100, 'y':200}
b = list(a.items())
print(b) #[('x', 100), ('y', 200)]
#########################################################
## dict itemini key ve value ya göre sıralama
#How to sort a dict by keys (Python older than 2.4):
keylist = mydict.keys()
keylist.sort()
for key in keylist:
    print "%s: %s" % (key, mydict[key])
#The results are the same as the above.

#How to sort a dict by value (Python 2.4 or greater):
for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)
## bir başka örnek
from collections import OrderedDict

 # regular unsorted dictionary
 d = {'banana': 3, 'apple':4, 'pear': 1, 'orange': 2}

 # dictionary sorted by key -- OrderedDict(sorted(d.items()) also works
 OrderedDict(sorted(d.items(), key=lambda t: t[0]))
OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])

 # dictionary sorted by value
 OrderedDict(sorted(d.items(), key=lambda t: t[1]))
OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])

 # dictionary sorted by length of the key string
 OrderedDict(sorted(d.items(), key=lambda t: len(t[0])))
OrderedDict([('pear', 1), ('apple', 4), ('orange', 2), ('banana', 3)])    
######################################################################