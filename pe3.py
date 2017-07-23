def find_factors(of_this_number):
    """Given a number, this method returns a list of its factors.
    
    Args:
        of_this_number:  An integer.
        
    Returns:
        A list of factors.
    """
    list_of_factors = []
    list_from_back = []
    end_of_range = of_this_number
    for number in range(1,end_of_range+1):
        if end_of_range % number == 0:
            append_this_number = end_of_range/number
            if append_this_number < number:
                break
            list_from_back.append(append_this_number)
            list_of_factors.append(number)
    return list_of_factors + list_from_back[::-1]
        
def find_prime_factors(of_this_number):
    """Given a number, this method returns a list of its prime factors.
    
    Args:
        of_this_number:  An integer.
        
    Returns:
        A list of prime factors.
    """
    list_of_factors = find_factors(of_this_number)
    list_of_primes = []
    for i, factor in enumerate(list_of_factors):
        if factor == 1:
            continue
        for previous_number in list_of_factors[1:i+1]:
            if factor % previous_number == 0 and factor != previous_number:
                break
            elif factor / previous_number == 1:
                list_of_primes.append(factor)
    return list_of_primes
            

def main():
    number = 0
    list_of_factors = find_factors(number)
    list_of_primes = find_prime_factors(number)

if __name__ == '__main__':
    main()

