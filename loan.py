salary=int(input("Salary: "))
age=int(input("age: "))
if(salary>=20000 and age>=25):
    loan=int(input("Required loan amount: "))
    if(loan<=50000):
        print("you are eligible for loan")
    else:
        print("Maximum amount of loan is 50000")
else:
    print("you are not eligible ")
