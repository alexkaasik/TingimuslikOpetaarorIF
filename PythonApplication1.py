'''
# Tri

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))
if a>0 and b>0 and c>0:
    if (a+b+c) == 180:
print("good")
    else:
print("bad")
'''

'''
# kalk

# setting none type
a=None
b=None
t=None
try:
    a = float(input("A: "))
    t = input("tehe: ")
    b = float(input("B: "))
except:
    pass

if t != None:
    if t in ["+","-","*","/","**","%","//"]:
        if a == 0 or b == 0:
            print("ERROR CAN'T DIVIDE zero")
        elif t == "+":
            print(a+b)
        elif t == "-":
            print(a-b)
        elif t == "*":
            print(a*b)
        elif t == "/":
            print(a/b)
        elif t == "**":
            print(a**b)
        elif t == "%":
            print(a%b)
        elif t == "//":
            print(a//b)
        else:
            print("Tundmatu märk")
'''

'''
# targv23 hinnad
group=input("group: ")
if group.lower() == "targv23":
    KeskHinnad=float(input("KeskHinnad: "))
    if KeskHinnad > 3.8:
        Puudumisip=int(input("Puudumisi: "))
        if Puudumisip < 15:
            print("good student")
        else:
            print("bad student")
    else:
        print("bad student")
else:
    print("not targv23")
'''

m=float(input("m: "))
n=float(input("n: "))
if m > n:
    v="m is heavier than n"
elif m == n:
     v="m=n"
elif m < n:
    v="m is lighter than n"
print(v)


if m > n:
    v="m is heavier than n"
else:
    if m == n:
         v="m=n"
    else:
        v="m is lighter than n"

print(v)

x=int(input("X:"))
if x%3==0:
    print("good")
else:
    print("bad")

for n in range(4):
    x=int(input("X:"))
    A=x%3
    if A==0:
        print("good")
    else:
        print("bad")