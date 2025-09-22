print("select one option")
print("1 -Addition")
print("2- Subtraction")
print("3 -Multiplication")
print("4-Division")
print("5- Exits")
option=int(input("Enter your option(1-5):"))
result=0
num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
if (option ==1):
    result=num1+num2
elif(option==2):
    result=num1-num2
elif(option==3):
    result=num1*num2
elif(option==4):
    result=num1/num2
elif(option==5):
    result="exits"
else:
    result="You choose invalid option"

print("The Result is :{}".format(result))
