a,b,c=input("Enter Numbers:").split(",")
x=int(a)
y=int(b)
z=int(c)
if x>=y and x>=z:
    print(f"The greatest number:{x}")
elif y>=x and y>=z:
    print(f"The greatest number:{y}")
else:
    print(f"The greatest number:{z}")