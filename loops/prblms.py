
#sum of first n nmbrs using while loop

# n=int(input("enter number : "))
# sum=0
# i=1
# while i<=n:
    
#     sum+=i
#     i+=1  
# print(f"sum of fisrt {n} numbers is ",sum)  


#sum of first n nmbrs using for loop

n=int(input("enter nmbr : "))
sum=0
for i in range(1,n+1):
    sum+=i
print(f"sum of first {n} numbers is {sum}")