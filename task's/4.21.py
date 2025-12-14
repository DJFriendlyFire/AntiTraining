def is_prime(n):
    if n > 1:
        mid = n // 2
        for i in range(2, mid):
            if n % i == 0:
                return False
        return True
    else:
        return False


print(is_prime(7))
print(is_prime(10))
