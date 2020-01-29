count=1
while count>0:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    sum = num1 + num2
    print (sum)
    print("Do you want to continue(y/n):")
    n=input()
    if (n=='y'):
        count=1
        continue
    else:
        count=0
        exit()
