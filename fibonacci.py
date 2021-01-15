#Program to print the Fibonacci series
n= int(input("Enter the number of terms: "))
n1,n2=0,1
print("The Fibonacci sequence is:")
print("The 1 term of the sequence is: ",n1)
print("The 2 term of the sequence is: ",n2)
for i in range(2,n):
   n3=n1+n2
   print("The",i+1,"term of the sequence is: ",n3)
   n1=n2
   n2=n3
