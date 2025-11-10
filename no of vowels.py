str=input("Enter: ")
a="AEIOUaeiou"
L=len(str)
c=0
for i in str:
    if(i in a):
        c=c+1
print(c)    
