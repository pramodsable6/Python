# Problem: check if the given string is palindrome or not

def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(check_palindrome('radar'))