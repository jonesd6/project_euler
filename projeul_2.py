# By considering terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.




def main():
    answer = 2
    term = 0
    term_1 = 1
    term_2 = 2
    while True:
        term = term_1 + term_2
        if term > 4000000:
            break
        term_1 = term_2
        term_2 = term
        answer += not term%2 and term
    print(answer)
if __name__ == '__main__':
    main()

