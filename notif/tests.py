from audioop import reverse
from django.test import TestCase

# Create your tests here.

# n = int(input().strip())

# arr = list(map(int, input().rstrip().split()))

# A = [1, 2, 3, 4]
# for i in reversed(range(len(A))):
#     print(A[i], end="")
n = input()    
phone_book = {"sam": 99912222, "tom": 11122222, "harry": 12299933}

for value in phone_book:
    if value in n:
        print(value,'=', phone_book[value])
    else:
        print("Not found")
