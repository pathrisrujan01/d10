#factorial of n using for loop

# n=int(input("enter nmbr : "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(f"factorial of {n} number is {fact}")


#factorial of n using while loop

n=int(input("enter the number: "))

i=1
fact=1
while i<=n:
    fact*=i
    i+=1
print(f"factorial of {n} is  {fact}")
