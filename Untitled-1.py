a=input("enter the value:")
a=int(a)
b=input("choose square or cube:")
b=(b.lower())
if"square"in b:
    c=a*a;
    print("square the value is:",c)
elif"cube"in b:
    c=a*a*a;
    print("cube value is:",c)
else:
    print("plz choose the correct path")