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
# n=int(input("Entr the number of inputs:"))
# longstk=0
# count=0
# for i in range(1,n+1):
#     stk=int(input(f"Enter the {i} streak:"))
#     if stk>0:
#         longstk+=1
#         if count>longstk:
#             longstk=count
#         else:
#             count=0
# print(longstk)

5.
# n=int(input("enter the inputs"))
# count=0
# for i  in range(1,n+1):
#     div=int(input("Enter the numbers:"))
#     if div%2==0:
#         count+=1
# print(count)

6.
# n=int(input("Enter the input:"))
# l=0
# c=int(input("enter thr 1 number"))
# for i in range(1,n+1):
#     num=int(input(f"Enter the {i} number:"))
#     if abs(num-c)>l:
#         l=abs(num-c)
#     else:
#         c=num
# print(l)

7.
# n=int(input("Enter the inputs:"))
# count=0
# for i in range(1,n+1):
#     sal=int(input("Enter the sal"))
#     if sal<=30000:
#         count+=1
# print(count)

8.
# n=int(input("Enter the inputs"))
# lsum=0
# lnum=0
# for i in range(1,n+1):
#     num=int(input("Enter the numbers:"))
#     nums=num
#     t=0
#     while nums!=0:
#         digit=nums %10
#         t=t+digit
#         nums=nums//10
#     if t>lsum:
#         lsum=t
#         lnum=num
# print(lnum)

9.
# n=int(input("Enter the inputs:"))
# count=0
# total=0
# for i in range(1,n+1):
#     nums=int(input("Enter th numbers:"))
#     if nums==0:
#         break
#     else:
#         total+=nums
#         count+=1
# print(total/count)

# 10.
# n=int(input("Enter the inputs:"))
# total=0
# count=0
# remin=0
# list1=[]
# for i in range(1,n+1):
#     nums=int(input("Enter the numbers:"))
#     list1=list1+[nums]
#     total+=nums
#     count+=1
# avg=total/count
# for i in list1:
#     if avg>i:
#             remin+=1
# print(remin)