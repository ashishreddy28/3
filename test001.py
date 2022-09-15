print("Input lengths of the triangle sides: ")
x = int(input("Enter the value for side a: "))
y = int(input("Enter the value for side b: "))
z = int(input("Enter the value for side c: "))

if x == y == z:
    print("")
    print("The Triangle is Equilateral")
elif x==y or y==z or z==x:
    print("")
    print("The Triangle is Isosceles")
elif x**2+y**2==z**2:
    print("")
    print("The Triangle is right angled")
else:
    print("")
    print("The Triangle is Scalene")


