#Variables
age = 25
name = "Saurav"
temperature = 36.5

#Data Types
a = 10        # int
b = 3.14      # float
name = "John" # string
is_active = True  # boolean
print(type(a))
print(type(name))

#Arithmetic Operators
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.33
print(a % b)   # 1 (remainder)
print(a ** 2)  # 100 (power)

#Comparison operators
x = 10
y = 20

print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True

#Logical Operators
a = 10
print(a > 5 and a < 20)  # True
print(a > 15 or a < 20)  # True
print(not(a > 5))        # False

#Inputs
name = input("Enter your name: ")
print(name)

#Conditional statements
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
    
#for Loops
for i in range(1, 6):
    print(i)
    
#while loops
i = 1
while i <= 5:
    print(i)
    i += 1
    
#(1) Temperature Converter (Celsius to Fahrenheit)
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

#(2) Simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)

#Client Project: Basic Data Processing Script (Average Temperature)
total = 0
days = int(input("Enter number of days: "))

for i in range(days):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    total += temp

average = total / days
print("Average Temperature:", average)
