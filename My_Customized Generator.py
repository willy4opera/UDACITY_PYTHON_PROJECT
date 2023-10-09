def My_Range(x):
    i = 0
    while i< x:
        yield i
        i += 1

for x in My_Range(5):
    print(x)