#Program to find the positive elements in the list
list1,list2,list3=[],[],[]
n=int(input("Enter the number of elements in the list: "))
for i in range(0,n):
    ele=int(input())
    if ele>0:
         list2.append(ele)
    elif ele<0:
        list3.append(ele)
    list1.append(ele)
print("The Elements in the list is: ",list1)
print("The positive elements in the list is: ",list2)
print("The negetive elements in the list is: ",list3)

