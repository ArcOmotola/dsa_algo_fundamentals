def factorial(n):
    assert n>=0 and int(n) == n, 'The number must be positive integer only!'
    if n in [0,1]:    #the basecase condition
        return 1
    else:
        return n * factorial(n-1)

print(factorial(8))

def countdown(n):
    print(n)
    if n <= 0:
        return
    else:
        countdown (n-1)

print(countdown(7))


# EXAMPLE OF USING A LOOP INSTEAD OF RECURSION
def factorial(n):
    result = 1
    for i in range(1, n + 1):
       result *= i
    return result

print(factorial(5))