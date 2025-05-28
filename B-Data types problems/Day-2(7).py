# Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

########### Write your code below ###############
# Insert k,v in my_dict
my_dict[k] = int(v)
print("Inserted")
# Print Inserted if inserted successfuly

########### Write your code above ###############

d = input()

########### Write your code below ###############
# Delete entry with key d from my_dict
if d in my_dict:
    del my_dict[d]
    print("Deleted")
else:
    print(-1)
# Else print -1
########### Write your code above ###############

p = input()

########### Write your code below ###############
# Print marks of given key p if key present, else print -1
print(my_dict.get(p, -1))
########### Write your code above ###############
