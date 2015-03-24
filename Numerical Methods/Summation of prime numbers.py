def is_prime(b):
    x = 0.0
    a = 0
    while x<b:
        x=x+1
        if (b/x)-int(b/x) == 0.0:
            a=a+1
    if a==2:
        return True
    else:
        return False

b = 1
prime_sum = 0
while b < upper_limit:
    b=b+1
    if is_prime(b):
        prime_sum = prime_sum + b
print(prime_sum)
