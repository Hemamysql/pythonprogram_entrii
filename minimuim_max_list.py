# find largest and smallest numer from a list
# find largest and smallest numer from a list
a = [100,-6,589,10,2,3,-999,18,23,9]

min=0
max=0
for i in range (len(a)):
        if a[i]<min:
            min=a[i]
        if a[i]>max:
            max=a[i]
print("smallest number=",min)
print("largest number=",max)
