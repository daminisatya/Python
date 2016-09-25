def digit_at(n):
    digits = 1
    n = n - 1
    while True:
        numbers = 9 * pow(10, digits-1) * digits
        if n > numbers: n = n - numbers
        else: break
        digits = digits + 1
    num = n / digits + pow(10, digits-1)
    return int(str(num)[n % digits])

print digit_at(1) * digit_at(10) * digit_at(100) * digit_at(1000) * digit_at(10000) * digit_at(100000) * digit_at(1000000)
