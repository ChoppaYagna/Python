n=int(input("N="))
N=n
f=1
while n > 0:
    f=f*n
    n -=1
print(f"Factorial of {N}:{f}")
    

#OR
#n=int(input("N="))
#f=1
#for i in range(1,n+1):
#   f=f*i
#print(f"Factorial of {N}:{f}")