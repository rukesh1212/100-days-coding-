# n=int(input("Enter the inputs"))
# count=0
# lcp=0
# for i in range(1,n+1):
#     nums=int(input(f"Enter the {i} numbers"))
#     if nums>=35:
#        count+=1
#        if count>lcp:
#            lcp=count
#     else:
#          count=0  
# print(lcp) 

2.
# n = int(input("Enter the number of inputs: "))
# p=0
# for i in range(n):
#     nums=int(input("ENtrt the numbers:"))
#     count=0
#     for j in range(1,nums+1):
#         if nums%j==0:
#             count+=1
#     if count==2:
#         if nums>p:
#             p=nums
# print(p)

3.
# n=int(input("Enter the inputs"))
# even=0
# for i in range(1,n+1):
#     nums=int(input("Enter the numbers:"))
#     num=[nums]
#     if i%2==0:
#         even+=i
# print(even)
        
4.
# n=int(input("Enter the inputs:"))
# defective=0
# good=0
# for i in range(1,n+1):
#     nums=int(input("Enter the products:"))
#     if nums>=50:
#         good+=1
#     if nums<=50:
#         defective+=1
# print(f'defictive ={defective}')
# print(f'good={good}')

5.
# n = int(input("Enter the inputs"))
# prev = int(input("ente 1 number"))
# maxinc = 0
# for i in range(2, n+1):
#     curr = int(input(f"Enter the {i} numbers"))
#     if curr - prev > maxinc:
#         maxinc = curr - prev
#     prev = curr
# print(maxinc)

6.
# n=int(input("Enter the inputs:"))
# ldig=0
# result=0
# for i in range(1,n+1):
#     nums=int(input(f"Enter the {1} numbers:"))
#     num=nums
#     count=0
#     while num>0:
#         count+=1
#         num=num//10
#     if count>ldig:
#         ldig=count
#         result=nums
# print(result)

# n=int(input("Enter the inputs:"))
# ans=0
# for i in range(1,n+1):
#     nums=int(input("Enter the numbers:"))
#     if nums%12==0:
#         ans+=1
# print(ans)

# n=int(input("Enter the inputs:"))
# count=0
# mcount=0
# for i in range(1,n+1):
#     nums=int(input("Enter the numbers:"))
#     if nums%2!=0:
#         count+=1
#         if count>mcount:
#             mcount=count
#     else:
#         count=0
# print(mcount)

# n = int(input("Enter a n: "))
# smallsum = 1000
# val = 0
# for i in range(n):
#     num = int(input("Enter a nums"))
#     temp = num
#     total = 0
#     while temp > 0:
#         total += temp % 10
#         temp //= 10
#     if total < smallsum:
#         smallsum = total
#         val = num
# print(val)

# n=int(input("Enter the balence:"))
# t=int(input("Enter the transactions:"))
# b=0
# for i in range(1,t+1):
#     tran=int(input("Enter the transactions:"))
#     b=tran+n
#     n=n+tran
#     print(f'balence={b}')
# print(f'fb={b}')

