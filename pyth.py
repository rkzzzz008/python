a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=a+b
print("The sum of", a, "and", b, "is", c)
d=int(input("Enter another number:"))
if d>c:
    result=d-c
else:
    result=c-d
print("The difference between", d, "and", c, "is", result)

printf("Program ended !")
