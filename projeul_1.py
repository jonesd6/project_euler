def pe_1(upper_bound):
    the_sum = 0
    for number in range(upper_bound):
        if number%3 == 0 or number%5 == 0:
            the_sum = the_sum + number
    return the_sum

def main():
    answer = pe_1(1000)
    print(answer)
if __name__ == '__main__':
    main()
