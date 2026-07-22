# 1.
# students=int(input("Enter no of students:"))
# count=0
# for i in range(1,students+1):
#     marks=int(input(f"Enter {i} stident marks:"))
#     if marks>=35:
#         count+=1
# print("the no of students score more than 35 is:{count}")

# 2.
# profitdays=int(input("Enter no of profit days:"))
# count=0
# for i in range(1,profitdays+1):
#     profit=int(input(f"Enter {i} profitdays:"))
#     if profit>=1000:
#         count+=1
# print(f"the no of profit days graterthan 1000 is:{count}")

# 3.
# num=int(input("Enter the numbers:"))
# max=0
# for i in range(num):
#     div=int(input("enter the numbers:"))
#     if div%5==0:
#         if div>max:
#             max=div
# if max>0:
#     print(f"the larges div of 5 {max}")
# else:
#     print("no possible")

# 4.
# num=int(input("enter the numbers:"))
# sum=0
# count=0
# for i in range(1,num+1):
#     even=int(input("enter the numbers:"))
#     if even%2==0:
#         sum+=even
#         count+=1
# if even>0:
#     avg=sum/count
#     print(avg)
# else:
#     print("no even number")

# 5.
# n=int(input("Enter the test:"))
# count=-1
# increase=0
# for i in range(1,n+1):
#     marks=int(input("Enter the marks:"))
#     if marks>increase:
#         count+=1
#         increase=marks
# print(f"increaswd markes {count}")

# 6.
# n=int(input("Enter the number"))
# count=0
# for i in range(1,n+1):
#     if n%i:
#         count+=1
# print(count)

7.
# n=int(input("Enter the number:"))
# sodd=0
# for i in range(1,n+1):
#     num=int(input("Enter the numbers:"))
#     odd=num
#     if num%2!=0:
#         if sodd==0:
#             sodd=num
#         elif num<sodd:
#             sodd=num
# print(f'smallodd:{sodd}')

8.
# n=int(input("Enter the number:"))
# count=0
# for i in range(1,n+1):
#     dig=int(input("Enter the numbers:"))
#     if dig%10==7:
#         count+=1
# print(f"the count{count}")

9.
# n=int(input("Enter the number:"))
# for i in range(1,16):
#     print(f"{n} x {i} = {n*i}")

10.
# n=int(input("Enter the input"))
# sum=0
# for i in range(1,n+1):
#     val=int(input("Enter the numbers:"))
#     if val>0:
#         sum+=val
#     else:
#         print(sum)
