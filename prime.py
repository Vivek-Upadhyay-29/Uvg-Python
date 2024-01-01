# # def pypart(n):
     
# #     # outer loop to handle number of rows
# #     # n in this case
# #     for i in range(0, n):
     
# #         # inner loop to handle number of columns
# #         # values changing acc. to outer loop
# #         for j in range(0, i+1):
         
# #             # printing stars
# #             print("* ",end="")
      
# #         # ending line after each row
# #         print("\r")
 
# # # Driver Code
# # n = 5
# # pypart(n)

# for i  in range (2):
#     print(i,end="")
a = 0
b = 1
n = int(input("enter a number"))
if n==1:
   print(a)
   
else:
     print(a)
     print(b)
     for i in range (1,n+1):
         c = a+b
         a = b
         b = c
         print(c)
     