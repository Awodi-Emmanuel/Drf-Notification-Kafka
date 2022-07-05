from audioop import reverse
from django.test import TestCase

# Create your tests here.

# n = int(input().strip())

# arr = list(map(int, input().rstrip().split()))

# A = [1, 2, 3, 4]
# for i in reversed(range(len(A))):
#     print(A[i], end="")
# x = int(input("Enter an input: "))

# dictt = {}

# for i in range(x):
#     text = input().split()
#     dictt[text[0]] = text[1]
# while True:
#     try:
#         inpt = input("Enter an input: ")
#         if inpt in dictt:
#             print(inpt+"="+dictt[inpt])
#         else:
#             print("Not found")
#     except EOFError:
#         break 

def recur_fact(n):
    if n == 2:
        return n 
    else:
        return n*recur_fact(n-2)
    
num = int(input("user input: "))
print("The factorial of ", num, "is", recur_fact(num))    