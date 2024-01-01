# name = "Vivek"
# age = 20
# print(f"Hello my name is{name} and i am {age} years old")
# input= input("Enter the {name}");
# print (f"input")

# def factorial(n):
#  if (n==0 or n==1):
#   return 1
#  else:
#   return n *factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))
def fibonaci(f):
 if(f==0 or f==1):
     return f
 else:
     return fibonaci(f-1)+ fibonaci(f-2)
print(fibonaci(2))
print(fibonaci(3))
print(fibonaci(4))
 
        