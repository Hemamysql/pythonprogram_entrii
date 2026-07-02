#armstrongnumber
count=0
n=int(input("enetr number"))
temp=n
if temp==0:
    print("enter a valid number")
else:
    while temp!=0:
        temp=temp//10
        count=count+1
print(count)
temp=n
total=0
while temp!=0:
    digit=temp%10
    total=total+digit**count
    temp=temp//10
print(total)
if n==total:
    print("armstrong number")
else:
    print("not an armstrong number")








