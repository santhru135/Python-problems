a=int(input("Enter the value: "))
sum=0
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
if(sum==a):
    print("It is a prime number")
else:
    print("It is not a perfect number")
      
