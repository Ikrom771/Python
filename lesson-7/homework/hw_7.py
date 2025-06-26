#1.
def is_prime(n):
    if n < 2:
        return False  # 0 and 1 are not prime
    for i in range(2, int(n**0.5) + 1):  # loop from 2 to sqrt(n)
        if n % i == 0:
            return False  # if divisible, it's not prime
    return True

print(is_prime(4))


#2. digit_sum(k) funksiyasi
def digit_sum(k):
    return(sum(int(digit) for digit in str(k)))
print(digit_sum(2234))

#3. powers
def powers(n):
    i = 1
    result = [] 
    while 2**i <= n:
        result.append(2**i)
        i += 1
    return result
print(powers(10)) 

