for number in range(2,100000):
    for factor in range(2,number+1):
        if number%factor == 0:
            break
        elif number==factor+1:
            break
            #print(number,'is prime')
