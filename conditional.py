# age = 28
# if(age>=18):
#     print("now you can vote")
#     print("now you can drive")

# light = "green"
# light = "yellow"
light = ""
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("wait")
else:
    print("light is broken")

marks =float(input("enter your marks:"))
if(marks>=80):
    grade = "A+"
elif(marks>=70 and marks<80):
    grade="A"
elif(marks>=60 and marks<70):
    grade="A-"
elif(marks>=50 and marks<60):
    grade="B"
elif(marks>=40 and marks<50):
    grade="C"
elif(marks>=33 and marks<40):
    grade="D"
else:
    grade = "F"
print("Your grade is",grade)


age = int(input("enter your age:"))
if(age>18):
    if(age<80):
        print("you can drive")
    else:
        print("you can't drive")
else:
    print("you can't drive")

num = int(input("enter an int number:"))
if(num%2==0):
    print(num,"is even number")
else:
    print(num,"is odd number")

num1 = int(input("enter 1st number:"))
num2 = int(input("enter 2nd number:"))
num3 = int(input("enter 3rd number:"))
if(num1>num2 and num1>num3):
    print(num1,"is greater than",num2,"and",num3)
elif(num2>num3):
    print(num2,"is greater than ",num1 ,"and",num3)
else:
    print(num3,"is greater than ",num1 ,"and",num2)

x = int(input("enter a number:"))
if(x%7==0):
    print(x,"is multiple of 7")
else:
    print(x,"is not multiple of 7")