prime_dict = {}

def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    if n in prime_dict:
        return prime_dict[n]
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def _is_valid(str_num):
    len_str = len(str_num)
    if len_str == 1:
        return is_prime(int(str_num))

    for count_index, index in enumerate(range(1, len_str)):
        left_num = int(str_num[:index])
        right_num = str_num[index:]
        if is_prime(left_num) and (_is_valid(right_num) or (is_prime(int(right_num)))) and not right_num.startswith('0'):
            return True
    return False


def is_valid(num, incall=True):
    str_num = str(num).strip()
    len_str = len(str_num)
    if is_prime(num) and len_str > 1:
        return _is_valid(str_num)
    return False


def total_primes(a, b):
    # your code here
    return [e for e in range(a, b+1) if is_valid(e)]


if __name__ == '__main__':
    print(total_primes(10, 100))
    print(total_primes(500, 600))
    print(total_primes(23, 37))
    print(total_primes(0, 20))
