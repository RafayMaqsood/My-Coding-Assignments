n = input("Enter a number between 1 to 100: ")
y = eval(input("Enter a base between 2 to 16: "))
z = int(n, y)
print (z)
x = bin(z)[2:]
print(x)
print(f"{n} in base {y} is: {z} in base 10 and {x} in base 2")


