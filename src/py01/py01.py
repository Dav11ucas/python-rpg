from audioop import reverse
from pickle import TRUE


def isPalindrome(number):
    number = str(number)
    if number[0::] == number[::-1]:
        print(f'{number} is palindrome')
    else:
        print(f'{number} is not a palindrome')

while TRUE:
    print("""
        checking if it is a palindrome number
    """)

    n = int(input('type a number to check: '))
    if n == 'end':
        break
    
    isPalindrome(n)
