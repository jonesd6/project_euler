import pe3

def create_palindrome(seed):
    """Creates a palindrome.
    
    Takes the seed input and creates a palindrome by reversing the seed and
    appending it the reverse to itself.
    
    Args:
        seed: An integer.
        
    Returns:
        A palindrome.
        
    """
    return int(str(seed) + str(seed)[::-1])

def count_3digit_factors(factors):
    num_of_3digit_factors = 0
    for factor in factors:
        if factor > 99 and factor < 1000:
            num_of_3digit_factors += 1
            if num_of_3digit_factors == 2:
                return True
    return False            

def main():
    seed = 997
    while seed > 0:
        palindrome = create_palindrome(seed)
        factors = pe3.find_factors(palindrome)
        mid_point = int(len(factors)/2 - 1)
        if factors[mid_point] > 99 and factors[mid_point] < 1000 and \
          factors[mid_point+1] > 99 and factors[mid_point+1] < 1000:
            print(palindrome)
            break
        #if count_3digit_factors([factors[mid_point], factors[mid_point+1]]):
        #    print(palindrome)
        #    break
        seed -= 1

if __name__ == '__main__':
    main()
