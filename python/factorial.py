r=int(input("Enter a number : "))
f=1
if r<0:
    print("Sorry, factorial does not exist for negative numbers")
elif r==0:
    print("The factorial is 1")
else:
    for k in range (1,r+1):
        f = f * r
        print("The factorial value is : ", f)
        break
    
    
        
        
