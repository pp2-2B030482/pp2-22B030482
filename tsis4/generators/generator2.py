def even_numbers_generator(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input(""))
even_numbers = even_numbers_generator(n)
print(",".join(str(e) for e in even_numbers))
