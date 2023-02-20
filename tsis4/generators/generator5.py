def countdown(n):
    while n >= 0:
        yield n
        n -= 1
        
n = int(input())
for i in countdown(n):
    print(i)
