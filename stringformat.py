""" 1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001"""
def print_formatted(number):
    # your code goes here
    width = str(bin(number)) #width[2:]
    for i in range(1,number+1):
        size = len(width[2:])
        sdec = str(i)
        soct = str(oct(i))
        shex = str(hex(i)).upper()
        sbin = str(bin(i))
        result = ' '*(size - len(sdec)) + sdec + ' '*(size+1 - len(soct[2:]))+ soct[2:] + ' '*(size+1 - len(shex[2:])) + shex[2:] + ' '*(size+1 - len(sbin[2:])) + sbin[2:]
        print (result)
        
