##ternary operator
a=4
b=2
max=a if a>b else b
print(max)

##2 Enumerate function
fruits =['apple','banana','orange']
for index,fruit in enumerate(fruits):
    print(index,fruit)

##3 zip function
list1=[1,2,3]
list2 =['a','b','c']
for x,y in zip(list1,list2) :
    print(x,y)

##4 list comprehesnion
squared_numbers = [x**2 for x in range(1, 6)]

print(squared_numbers)
#[1, 4, 9, 16, 25]

##5 lamba function
add =lambda x,y,z :x+y+z
result=add(3,4,2)
print(result)
