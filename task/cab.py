count=1
while count>0:
    src=int(input("Enter your source:"))
    dest=int(input("Enter your destination:"))
    km=dest-src
    print("1.Mini\n2.Macro\n3.Prime\n")
    print("Enter tour choice:");
    n=int(input())
    while True:
        if(n==1):
            print("Kilometers:",km)
            price=km*10
            print("Price:",price)
            print("Thank you!!!\n\n")
            break
        elif(n==2):
            print("Kilometers:",km)
            price=km*20
            print("Price:",price)
            print("Thank you!!!\n\n")
            break
        elif(n==3):
            print("Kilometers:",km)
            price=km*50
            print("Price:",price)
            print("Thank you!!!\n\n")
            break
        else:
            print("Invalid opton!!!")
            break
    count=1
    continue
else:
    exit()
