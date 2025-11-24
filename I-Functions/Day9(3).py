def roots(a,b,c):
    r1=0
    r2=0
    d=(b**2)-4*a*c
    r1=(-b+(d**(0.5)))/2*a
    r2=(-b-(d**(0.5)))/2*a
    print(f"roots:{r1},{r2}")
a=int(int(input("a=")))
b=int(int(input("b=")))
c=int(int(input("c=")))
roots(a,b,c)