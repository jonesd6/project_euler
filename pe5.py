import pe3

def find_primes(number):
    """Find the prime number less than or equal to the number passed.
    
    Args:
        number: The max number to use.
        
    Returns:
        list_of_primes: A list of prime numbers less than or equal to 'number'.
        
    """
    list_of_primes = []
    for inc in range(1, number+1):
        if len(pe3.find_factors(inc)) == 2:
            list_of_primes.append(inc)
    return list_of_primes

def test(number):
    if number % 2 == 0 and \
       number % 3 == 0 and \
       number % 4 == 0 and \
       number % 5 == 0 and \
       number % 6 == 0 and \
       number % 7 == 0 and \
       number % 8 == 0 and \
       number % 9 == 0 and \
       number % 10 == 0 and \
       number % 11 == 0 and \
       number % 12 == 0 and \
       number % 13 == 0 and \
       number % 14 == 0 and \
       number % 15 == 0 and \
       number % 16 == 0 and \
       number % 17 == 0 and \
       number % 18 == 0 and \
       number % 19 == 0 and \
       number % 20 == 0:
        return True
    else:
        return False

def find_nonprimes(number, list_of_primes):
    list_of_nonprimes = []
    for prime in list_of_primes:
        if number % prime == 0:
            list_of_nonprimes.append(number / prime)
    return list_of_nonprimes

def find_composites(k, list_of_primes):
    list_of_composites = []
    for i in range(1, k+1):
        if i not in list_of_primes:
            list_of_composites.append(i)
    return list_of_composites           

def main():
    k = 20
    product = 1
    list_of_primes = find_primes(k)
    print(k)
    print(list_of_primes)
    for i in range(1,k+1):
        #print(i)
        list_of_nonprimes = find_nonprimes(i, list_of_primes)
        #print(list_of_nonprimes)
    list_of_composites = find_composites(k, list_of_primes)
    
    for number in list_of_composites:
        print(number, pe3.find_factors(number))
    """
    for i in list_of_primes:
        product *= i
    print(product)
    product *= 24
    for i in range(1, k):
        if product % i == 0:
            print('{0}: True'.format(i))
        else:
            print('{0}: False'.format(i))
    print(test(product))
    """

if __name__ == '__main__':
    main()