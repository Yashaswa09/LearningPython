# Fibonacci series:
# the sum of two elements defines the next
# a =0

# while (a==0):
#     print("hello world")
    
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b