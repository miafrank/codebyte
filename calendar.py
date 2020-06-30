input_str = "I Love Code"
print(input_str[::-1])


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n * recur_factorial(n - 1)


print(recur_factorial(4))
