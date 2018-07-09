if __name__ == '__main__':
    s = input()
    alphanum = 0
    alpha = 0
    digit = 0
    upper = 0
    lower = 0
    for c in s:
        if c.isalnum():
            alphanum = 1
        if c.isalpha():
            alpha = 1
        if c.isdigit():
            digit = 1
        if c.islower():
            lower = 1
        if c.isupper():
            upper = 1
    if(alphanum == 1):
        print (True)
    else:
        print (False)
    if(alpha == 1):
        print (True)
    else:
        print (False)
    if(digit == 1):
        print (True)
    else:
        print (False)
    if(lower == 1):
        print (True)
    else:
        print (False)
    if(upper == 1):
        print (True)
    else:
        print (False)