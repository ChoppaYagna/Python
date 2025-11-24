m=int(input("Math:"))
s=int(input("Sci:"))
e=int(input("eng:"))
Tot=m+s+e
avg=Tot/3
per=(Tot/300)*100
if per >90:
    grade="A"
elif per >80:
    grade="B"
elif per >70:
    grade="C"
else:
    grade="Pass"
print(f"Total:{Tot}\nAverage:{avg} \nGrade:{grade}")