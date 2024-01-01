# for i in range (6):
#     print(i)
# else :
#     print("sorry")
def print_patter(row):
    for i in range(row,-0,-1):
     for j in range (i):
       print("$", end="")
       print("\n")
         
row=4
print_patter(row)          