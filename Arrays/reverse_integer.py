# Problem: reverse the given integer in an efficient way

def reverse_integer(n):

    reversed_integer = 0
    remainder = 0
    
    while n > 0:
        remainder = n % 10                      # get last digit
        n = n // 10                             # remove last digit from n
        reversed_integer = reversed_integer * 10 + remainder      

    print(reversed_integer)


if __name__ == '__main__':
    n = int(input('Enter an integer: '))
    reverse_integer(n)
