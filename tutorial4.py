########### Module import Syntax Python Tutorial ###########
import statistics
example_list = [5,2,5,6,1,2,6,7,2,6,3,5,5]
print(statistics.mean(example_list))
###
import statistics as s
print(s.mean(example_list))
##
from statistics import mean
# so here, we've imported the mean function only.
print(mean(example_list))

# and again we can do as
from statistics import mean as m
print(m(example_list))
###
from statistics import mean, median
# here we imported 2 functions.
print(median(example_list))

##
from statistics import mean as m, median as d

print(m(example_list))
print(d(example_list))
##
from statistics import *

print(mean(example_list))

###### Argparse for CLI Intermediate Python Tutorial part 3
import argparse
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', type=float, default=3.0,
                        help='What is the first number?')
    parser.add_argument('--y', type=float, default=21.0,
                        help='What is the second number?')
    parser.add_argument('--operation', type=str, default='mul',
                        help='What operation? Can choose add, sub, mul, or div')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))


def calc(args):
    if args.operation == 'add':
        return args.x + args.y
    elif args.operation == 'sub':
        return args.x - args.y
    elif args.operation == 'mul':
        return args.x * args.y
    elif args.operation == 'div':
        return args.x / args.y


if __name__ == '__main__':
    main()


########### list comprehension
input_list = [5,6,2,1,6,7,10,12]

def div_by_five(num):
    if num % 5 == 0:
        return True
    else:
        return False

xyz = [i for i in input_list if div_by_five(i)]
print(xyz)
### nested loop
[[print(i,ii) for ii in range(3)] for i in range(5)]
####Enumerate Intermediate Python 
## dict enumarate
example_dict = {'left':'<','right':'>','up':'^','down':'v',}
[print(i,j) for i,j in enumerate(example_dict)]

##### Python's Zip function
x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']
print(*zip(x,y,z))
## two list to dict with zip function
names = ['Jill','Jack','Jeb','Jessica']
grades = [99,56,24,87]

d = dict(zip(names,grades))
print(d)
##### aşağıdaki kod x 'de değişikliğe neden olur
x = [1,2,3,4]
y = [7,8,3,2]
z = ['a','b','c','d']

#[print(x,y,z) for x,y,z in zip(x,y,z)]
for x,y,z in zip(x,y,z):
    print(x,y,z)
print(x)
#######  More on Generators with Python
## aşağıdaki kodda sadece 3.döngü kırılır, diğerleri devam eder
CORRECT_COMBO = (3, 6, 1)
found_combo = False
for c1 in range(10):
    for c2 in range(10):
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo:{}'.format((c1, c2, c3)))
                break

### aşağıdaki kodda hedefe ulaşıldıktan sonra döngü 3 döngü içinde kırılır
CORRECT_COMBO = (3, 6, 1)
found_combo = False
for c1 in range(10):
    if found_combo:
        break
    for c2 in range(10):
        if found_combo:
            break
        for c3 in range(10):
            if (c1, c2, c3) == CORRECT_COMBO:
                print('Found the combo:{}'.format((c1, c2, c3)))
                found_combo = True
                break
### yield kullanımı yukarıdaki gibi çalışır
def combo_gen():
    for c1 in range(10):
        for c2 in range(10):
            for c3 in range(10):
                yield (c1, c2, c3)

for (c1, c2, c3) in combo_gen():
    print(c1, c2, c3)
    if (c1, c2, c3) == CORRECT_COMBO:
        print('Found the combo:{}'.format((c1, c2, c3)))
        break


#### Headless Error Handling Python Tutorial
import sys

try:
    a+b
except:
    print(sys.exc_info()[0])
    print(sys.exc_info()[1])
    print(sys.exc_info()[2].tb_lineno)
    print('Error: {}. {}, line: {}'.format(sys.exc_info()[0],
                                         sys.exc_info()[1],
                                         sys.exc_info()[2].tb_lineno))



#<class 'NameError'>
#name 'a' is not defined
#4
#Error: <class 'NameError'>. name 'a' is not defined, line: 4