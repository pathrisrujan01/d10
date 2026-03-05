# for i in range(1,11):
#     print(i)

# i=1
# while i<=10:
#     print(i)
#     i+=1


# for i in range(1,21,2):
#     print(i)

# i=1
# while i<=20:
#     if(i%2==0):
#         print(i)
#     i+=1

# n=int(input("enter nmbr: "))
# for i in range(1,11):
#     print(f"{n}x{i}=",i*n)

# n=int(input("enter nmbr: "))
# i=1
# while i<=10:
#     print(f"{n}x{i}=",i*n)
#     i+=1

# n=100
# i=1
# sum=0
# while(i<=n):
#     sum+=i
#     i+=1
# print(sum)


# n=100
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# str="Python"
# for i in str:
#     print(i)


# s="python"
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1


# str="aeroplane"
# count=0
# for i in str:
#     if i.lower() in "aeiou":
#         count+=1
# print(count)
        
# s="data struvture"
# count=0
# for i in s:
#     if i in "aeiou":
#         count+=1
# print("no of vowels in" ,s, "are" ,count)

# s="srujan"
# i=0
# count=0
# while i<len(s):
#     if s[i].lower() in "aeiou":
#         count+=1
#     i+=1
# print(count)



# i=10
# while i>=1:
#     print(i)
#     i-=1


# n=5
# i=1
# sum=0
# while i<=n:
#     sum+=i
#     i+=1
# print(sum)


# n=2
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print(sum)


# n=222
# total=0
# while n>0:
#     b=n%10
#     total+=b
#     n=n//10
# print(total)

# num=1234
# reverse=0
# while num>0:
#     a=num%10
#     reverse=reverse*10+a
#     num=num//10
# print(reverse)


# s="123"
# sum=0
# for i in s:
#     sum+=int(i)
# print(sum)


# crct_password="python123"
# while True:
#     password=input("enter password:")
#     if password==crct_password:
#         print("crct")
#         break
#     else:
#         print("wrong")




# n=5
# i=1
# while i<=10:
#     print(f"{n}x{i}=",i*n)
#     i+=1


# for i in range(5,0,-1):
#     print("*"*i)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
    
#     if x == "banana":
#       break
#     print(x)



# movies=["eega", "rrr", "kgf", "war", "hero"]
# cities=["goa","vizag","hyd","manali"]

# # def length(list):
#     print(len(list))

# length(movies)
# length(cities)
# def sin_line(list):
#     for i in list:
#         print(i , end=" ")
        

# sin_line(movies)

# sin_line(cities)


# def fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     print(fact)
"""
 fact(5)
 """
 

# def conv(usd):
#     inr=usd*91
#     print(usd,"usd", inr,"inr")

# conv(2)
# list=['ss','es','we']
# def total(list):
#   for i in list:
#     print(i,end=" ")
    
# total(list)


# def factorial(n):
#     i=1
#     fact=1
#     while i<=n:
#         fact*=i
#         i+=1
#     print(fact)


# factorial(5)

# def converter(usd):
#     inr=usd*80
#     print(usd,"usd is equal to " , inr , "rupees")
    
# converter(5)


# def evod(n):
#     if n%2==0:
#         print(n , "is even")
#     else:
#         print(n , "is odd")

# evod(5)
# evod(8)


# def num(n):
#     if n==0:
#         return
#     print(n)
#     num(n-1)

# num(10)


# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * fact(n-1)

# print(fact(5))


# def num(n):
#     if n==0:
#         return 0
#     return n+num(n-1)

# print(num(5))


#armstrong
# num=1634

# num1=num
# sum=0
# n=len(str(num))
# while num>0:
#     ld=num%10
#     sum=sum+ld**n
#     num=num//10
# print(sum)
# if num1==sum:
#     print(num1,"is armstrong")
# else:
#     print(num1,"is not armstrong")


# sum=0
# mul=1
# for i in range(1,31):
#     if i%2==0:
#         sum+=i
#     else:
#         mul*=i
# print(sum)
# print(mul)




""" str='something'
i=-1
while i>=-9:
     print(str[i])
     i-=1  """




""" Triangle = False
a=60
b=60
c=9
if Triangle == True:
    print("it is triangle");
    if a+b+c == 180:
        print("eq");
    elif a==b or b==c or c==b:
        print("iso");
    else:
        print("sc");
if Triangle == False:
    print("it is not a triangle"); """
         

# temp = -9
# if temp>0:
#     if temp < 30:
#         print("m");
#     if temp>30:
#         print("hot");
# else:
#     print("its frezing");

# x=1234
# count=0
# while x>0:
#     ld=x%10
#     count+=1
#     x=x//10
# print(count)

n=81
i=1
# x=1
# sum=0
while i<=n//2:
    if n%i == i:
        print("sq")
        i+=1
    else:
        break
       
    



     

