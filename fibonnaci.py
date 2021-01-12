num=int(input("enter a number"))
n1=0
n2=1
count=0
if num<1:
    print("please enter a positive number")
elif num==1:
    print(n1)
else:
    print("the fibonnaci series:")
    while count<num:
        print(n1)
        nterm=n1+n2
        n1=n2
        n2=nterm
        count+=1

