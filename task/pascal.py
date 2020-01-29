def pascal(n):
    a=1
    for c in range(1,n+1):
        a = a*c
    return a

rows = int(input("Enter the number of rows : "))
for i in range(0, rows):
    for j in range(1, rows-i):
        print("  ", end="")
    for k in range(0, i+1):
        b = int(pascal(i)/(pascal(k)*pascal(i-k)))
        print("  ", b, end="")
    print()
