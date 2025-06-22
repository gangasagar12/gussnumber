import random
n=random.randint(1,100)
a=-1
gusses=0
while(a!=n):
    gusses+=1
    a=int(input("guss a number: "))
    if (a>n):
        print("lower number please")
    else:
        print("higher number please")

print(f" you have gusses the correct number in a t { gusses}")