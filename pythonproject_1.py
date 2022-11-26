print("\nWelcome to the E-mail-Slicer™\n")
a=int(input("How many Emails would you like to slice?: "))



for i in range(1,a+1):
    b=str(input("\nEmail: "))
    l=len(b)
    d=0
    
    for i in range(1,l):
        if b[i]=='@':
            d=i
            break
    
    if d>0:
        a=""
        for i in range(0,d):
            a+=b[i]
        print("User Name: ",a,end="")
        m = ""
        
        for j in range(d+1,len(b)):
            m+=b[j]
        print("\nDomain: ",m,end="",)
    
    else: 
        print('Invalid E-mail given')

        print()



print("\nThanks for Using E-mail-Slicer™ :)")
