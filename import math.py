import math
print("......INTEGER.......")
a=20
b=10
print("a=",a)
print("b=",b)
print("addition=",a+b)
print("subtraction=",a-b)
print("multiplication=",a*b)
print("division=",a/b)
print("floor division=",a//b)
print("modulus=",a%b)
print("power=",a**b)
print()
print("........FLOAT..........")
x=12.98
y=32.01
print("x=",x)
print("y=",y)
print("addition=",x+y)
print("subtraction=",x-y)
print("multiplication=",x*y)
print("division=",x/y)
print()
print("........complex......")
u=4+5j
v=6+6j
print("addition=",u+v)
print("subtractio=",u-v)
print("multiplication=",u*v)
print()
print("...........string........")
name="Hello World"
print("name")
print("Length=",len(name))
print("Upper=",name.upper())
print("Lower=",name.lower())
print("Replace=",name.replace("Python","Advanced","Python"))
print("slice",name[0:-1])
print("......INTEGER.......")
a=20
b=10
print("a=",a)
print("b=",b)
print("addition=",a+b)
print("subtraction=",a-b)
print("multiplication=",a*b)
print("division=",a/b)
print("floor division=",a//b)
print("modulus=",a%b)
print("power=",a**b)
print()
print("........FLOAT..........")
x=12.98
y=32.01
print("x=",x)
print("y=",y)
print("addition=",x+y)
print("subtraction=",x-y)
print("multiplication=",x*y)
print("division=",x/y)
print()
print("........complex......")
u=4+5j
v=6+6j
print("addition=",u+v)
print("subtractio=",u-v)
print("multiplication=",u*v)
print()
print("...........string........")
name="Hello World"
print("name")
print("Length=",len(name))
print("Upper=",name.upper())
print("Lower=",name.lower())
print("Replace=",name.replace("Python","Advanced","Python"))
print("slice",name[0:-1])
print()
print(".......LIST......")
numbers=[10,20,30,40]
print(numbers)
numbers.append(50)
numbers.insert(2,25)
numbers.remove(20)

print()
print("...........TUPLE......")

t=(100,200,300)

print(t)

print("Length=",len(t))
print("Maximum=",max(t))
print("Minimum=",min(t))

print()

print(".......Dictionary......")

student={
    "Roll":101,
    "Name":"Amit",
    "Marks":89,
}
print(student)

print(student.keys())
print(student.values())
print(student.items())

print()

print(".......SET........")

s={2,4,6,8}
print(s)
s.add(10)
print()
print(".......FROZEN SET......")
fs = frozenset([1,2,3,4,5])
print(fs)
print()
print(".......BOOLEAN......")
flag=True
print(flag)
print(type(flag))
print()
print("......NONE TYPE......")
value=None
print(value)
print(type(value))
print()
print("............BUILT IN FUNCTION........")
print(abs(-45))
print(round(12.6789,2))
print(pow(5,3))
print(divmod(20,3))
print(bin(15))
print(hex(255))
print(type(a))
print()
print(".......MATH MODULE......")
print("Square Root=",math.sqrt(25))
print("Factorial=",math.Factorial(5))
print("Power=",math.piow(2,5))
print("Ceil=",math.ceil(4.3))
print("Floor=",math.floor(4.8))
print("Pi=",math.pi)
print("sin(90)=",math.sin(math.radians(90)))
print("cos(0)=",math.cos(math.radian(0)))
print("Log=",math.log(10))