"""------------.|.------------
   ---------.|..|..|.---------
   ------.|..|..|..|..|.------
   ---.|..|..|..|..|..|..|.---
   ----------WELCOME----------
   ---.|..|..|..|..|..|..|.---
   ------.|..|..|..|..|.------
   ---------.|..|..|.---------
   ------------.|.------------"""

n, m = map(int, input().split())
i = 0
while (i < n/2-1):
    print (('.|.'*(2*i+1)).center(m,'-'))
    i = i+1
print('WELCOME'.center(m,'-'))
i = n//2
while (i > 0):
    print (('.|.'*(2*i-1)).center(m,'-'))
    i = i-1
    
