#sum of integers 
# i=0
# sum=0
# while i<5:
#     sum =sum+i
#     i=i+1
# print(sum)
#sum of odd integers
# i=0
# esum=0
# while i<100:
#     esum =esum+i
#     i=i+2
#     print(i)
# print(esum)
i=0
osum=0
esum=0
while i<100:
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
    i=i+1
print(esum)
print(osum)
        

