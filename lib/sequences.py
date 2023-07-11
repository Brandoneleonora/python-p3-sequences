#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = []
    count = 0
    n1, n2 = 0, 1

    if length == 0:
        print([])
    elif length == 1:
        fib_list.append(n1)
        print(fib_list)
    elif length == 2:
        for n in range(length):
            fib_list.append(n)
        print(fib_list)
    else:
        while count < length:
            fib_list.append(n1)
            new_number = n1 + n2
            n1 = n2
            n2 = new_number
            count += 1
        print(fib_list)
