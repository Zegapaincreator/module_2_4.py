numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)-1):
    is_prime = True
    if numbers[i] < 2:
        is_prime = False
    else:
        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                is_prime = False
                break
    if is_prime:
        primes.append(numbers[i])
    else:
        if numbers[i] != 1:
            not_primes.append(numbers[i])
        else:
            numbers.remove(numbers[i])

print("Primes:", primes)
print("Not Primes:", not_primes)
