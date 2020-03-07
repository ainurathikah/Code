#Session 1.0

#Exercise 1
print('To learn about universe')

#Exercise 2
name="Ainur Athikah Binti Zulkeflee"
Age=21
print('My name is',name)

#1.4.1 Global Variables
someVar=3.14
def someFunc(radius):
    print('radius=',2*someVar*radius,'metre(s)')   

#1.4.2 Naming Conventions
someNumber=5
some_number=6

#1.5 Input
number=input('7')
print('num')

#2.1.1 Boolean(bool)
v=15
w=0
print(bool(v))
print(bool(w))

#2.1.2.1 String Manipulation Methods
a='Map of the Soul'
print(a[3:7])
print(a[-5:-3])
print(len(a[2:-7]))

#2.1.2.2 String Combination, Check
a='Boruto is just a Naruto reboot'
b=a+'and Sakura was best girl'
c='Naruto'
check=c in b
print(check)

#2.1.3 Numbers (int,float,complex)
x=15
y0=15.
y1=15.0202020202000
z=15+2j
print(type(x))
print(type(y0))
print(type(int(y0)))
print(type(y1))
print(type(z))

#2.1.4.1 lists
someList=['stop','i','could','have','dropped','my','croissant']
print(someList[0])
print(someList[2:4])#yang ke 4 dia tak copy

gravityReading=[10.1,8.5,9.8,16.3,9.95]
del gravityReading[0]#delete 0
gravityReading.remove(16.3)# remove 16.3
print(gravityReading)

gravityReading=[10.1,8.5,9.8,16.3,9.95]
enumList=enumerate(gravityReading)
print(enumList)

for i, reading in enumerate(gravityReading):
        print(i, reading)
        
#2.1.4.1.1 List Operations
mean=0
for reading in gravityReading:mean +=reading
mean=mean/len(gravityReading)
print(mean)

#2.1.4.1.2 Nested Lists
trajpoints=[[2,3,4,5],[3,6,6,3]]
for dim in trajpoints: 
    print(dim)
    
#2.1.4.3 Dictionaries

isSimulate= True
if isSimulate:
        print('This is a simulation')
        
v=6
w=v
if v == w:
    print('v is equal to w')
if w is v:
    print('v is w')






