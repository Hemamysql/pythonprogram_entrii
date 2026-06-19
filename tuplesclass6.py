list
# collectio of data,square bracket,comma sepereated
# can contain any data of any size
# data[1,2,3,4]
# b=[1,1.5,"mogmn",[12,3,3],true]
# ordered
# indexed
# list[start:stop:step]
#a=[3,1,4,8,3,6,5,0,111]
#print(type(a))
# print(a[4])
# print(a[0:4])
# print(a[2:10:3])
# print(a[:7])
# print(a[1:])
# print(a[::])
# print(a[::-1])
#print(a[:16])
#list is mutable ,string not mutable,list are dynamic(list grows /shrink)
#a[0]='mohan'
#a[8]='das'
#print([a])
#append -add element in the last 
#a=[1,2,3,4,5,6,53]
# a.append("hema")
#print(a)
#insert- need index and item 
# a.insert(1,"hema")
# print(a)
#remove(item )
#a=[1,2,3,6,8,9,55,33]


# a.remove(1)
# print(a)
#pop-removes last element
#pop(index)
# a.pop()
# a.pop()
# a.pop()
# print(a)
# a.pop(2)
# print(a)

# a=(3,1,4,8,3,6,5,0,111)
#print(type(a))
#LIST ARE MUTABLE < BUT TUPLE IS IMMUTABLE 

#for i in range(0,len(a)):
#collection of data -iterable
    #print(i,a[i])
#print(len(a))
# for i in a:
#     print(i)
# name="vaisakhan"
# for i in name:
#     print(i)
#set- unordered,mutable
#un indexed
#does not allow duplicate values
# a={22,33,333,663,373,89,89,79,333,33,23,32}
# print(len(a))
# print(a)
# b={665,663,33,8,353,638}
# print(a.intersection(b))#intersection
# print(a.union(b))#union
# print(a-b)#differnce common eleimated from a
# print(b-a)#common elimainted from b
#dictory a={"key":value,key:value:},mutable,key should be unique, mutable
#key should be non mutable
user={"name":"hema","age":29,"location":"kochi"}
print(user)
print(user['age'])
mydata={}
mydata["name"]="hemaq"

mydata["age"]=34
mydata["place"]="palakkad"
print(mydata)




