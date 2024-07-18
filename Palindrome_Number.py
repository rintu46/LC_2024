
def palindrome(x):
    if x < 0 :
        return False

    x = str(x)
    rev = x[::-1]
    print('rev: ', rev)

    if rev == x:
        return True
    else:
        return False


# user inputs
nums = 121

result = palindrome(nums)
print('result: ', result)


 