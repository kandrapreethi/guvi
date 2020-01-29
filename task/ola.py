def taxi():
    while True:
        src=int(input("Enter your source:"))
        dest=int(input("Enter your destination:"))
        km=dest-src
        print("1.Mini\n2.Macro\n3.Prime\n")
        print("Enter tour choice:");
        n=int(input())
        if(n==1):
            mini(km)
        elif(n==2):
            macro(km)
        elif(n==3):
            prime(km)
        else:
            print("Invalid option")
        continue
    return true

def mini(km):
    print("Kilometers:",km)
    price=km*10
    print("Price:",price)
    print("Thank you!!!\n\n")
    taxi()
    return true

def macro(km):
    print("Kilometers:",km)
    price=km*20
    print("Price:",price)
    print("Thank you!!!\n\n")
    taxi()
    return true

def prime(km):
    print("Kilometers:",km)
    price=km*50
    print("Price:",price)
    print("Thank you!!!\n\n")
    taxi()
    return true
print("welcome")
taxi()
