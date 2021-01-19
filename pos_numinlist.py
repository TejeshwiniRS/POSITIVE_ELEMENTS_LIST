lst=[]
list1=[]
n=int(input("Enter no.of elements in the list: "))
for i in range(0,n):
    elements=int(input())
    lst.append(elements)
print("Input:list1=")
print(lst)
for num in lst:
    if(num>=0):
        list1.append(num)
print("Output:")
print(list1)
