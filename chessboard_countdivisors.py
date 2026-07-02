# for i in range(1,9):
#     if i%2==0:
#         print("B W B W B W B W",end="")
#         print()
#     else:
#         print("W B W B W B W B",end="")
#         print()

l,r,k = map(int, input().split())
count=0
for i in range(l,r+1):
    if i%k==0:
        count=count+1
print(count)