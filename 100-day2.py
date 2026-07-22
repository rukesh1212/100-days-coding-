# months=int(input("Enter the months:"))
# profits=0
# count=0
# for i in range(1,months+1):
#     prof=int(input("Enter the profits:"))
#     if prof>profits:
#         profits=prof
#         count=i
# print(f"heigest profit is:{profits} in {count} months")

# 2.
# n=int(input("Enter the number"))
# count=0
# for i in range(1,n+1):
#     sq=int(input("Enter the numbers"))
#     num=int(sq**0.5)
#     if num*num==sq:
#         count+=1
# print(count)

3.
# a=int(input("Enter the input1:"))
# b=int(input("Enter 2nd input:"))
# sum=0
# for i in range(a,b+1):
#     if i%7==0:
#         sum+=i
# print(sum)

4.
n=int(input("Entr the number of inputs:"))
longstk=0
count=0
for i in range(1,n+1):
    stk=int(input(f"Enter the {i} streak:"))
    if stk>0:
        longstk+=1
        count+=1
print(count)
