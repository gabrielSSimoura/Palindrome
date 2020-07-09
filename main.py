# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)


def isPalindrome(userString):
    userReverseString = userString[::-1]
    if (userReverseString.lower() == userString.lower()):
        print("It's Palindrome")
        exit()
    else:
        print("It's not Palindrome")


def main():
    userString = input("Write some text here: ")
    isPalindrome(userString)


main()
