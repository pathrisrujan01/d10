#print the elemnts of list using a loop
# [1,4,9,16,25,36,49,64,81,100]

# list=[1,4,9,16,25,36,49,64,81,100]
# for el in list:
#     print(el)




tup=(1,4,9,16,25,36,49,64,81,100)
idx=0
for n in tup:
    if(n==64):
        print("found",idx)
    idx+=1
    print(n)