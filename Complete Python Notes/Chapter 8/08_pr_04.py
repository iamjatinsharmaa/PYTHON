# n! = (n-1)! * n 
# sum(n) = sum(n-1) + n

n = int(input("Enter the required number "))
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n - 1)

h = sum(n)
print(h)
