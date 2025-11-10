str=input("Enter the value: ")
L=len(str)
L1=[]
L2=[]
for i in range(L):
    if(i%2==0):
        L1.append(str[i])
    else:
        L2.append(str[i])
print("Even position: ",L1)
print("Odd position: ",L2)
