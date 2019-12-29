def myfunc():
    even = 0
    odd = 0
    for i in range(1,int(input())):
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("even = ", even)
    print("odd = ", odd)
myfunc()