count = 1

while count <= 10:
    print(count, end=" ")
    count += 1

for n in range(1, 11):
    print(n, end=" ")

def greet():
    name = input("Please enter your name: ")
    print("Hi", name)
greet()

def greet(name):
    print("Hi", name)   
greet("Yoggith")

x= "Ali"
greet(x)

def total(a, b, c):
    sum= a+b+c
    print("Total is", sum)
total(20,30,10)

def greater (a, b):
    if a >= b:
        return a
    else:
        return b
greater(10, 20)

n1 = 10
n2 = 15
gr = greater(n1,n2)
print ("greater number is", gr)