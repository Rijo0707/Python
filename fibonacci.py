#Program to print the Fibonacci series
n= int(input("Enter the number of terms: "))
n1=0
n2=1
count=0
if n<=0:
   print("Invalid Input!!")
elif n==1:
   print("The Fibonacci sequence is:")
   print(n1)
else:
   print("The Fibonacci sequence is:")
   while count<n:
       print(n1)
       n3=n1+n2
       n1=n2
       n2=n3
       count+=1
