def minion_game(string):
    # your code goes here
    #using LIST COMPREHENSIONS gives N^2 complexity so runtime errors
    """vowels = []
    conso = []
    subs = [string[i:j+1] for i in range(len(string)) for j in range(i,len(string))] #N^2 complexity
    for i in subs:
        if(i[0] == 'A' or i[0] == 'E' or i[0] == 'I' or i[0] == 'O' or i[0] == 'U' ):
            vowels.append(i)
        else:
            conso.append(i)
    cresult = len(conso)
    vresult = len(vowels)
    if(cresult > vresult):
        print ("Stuart " + str(cresult))
    elif(cresult < vresult):
        print ("Kevin " + str(vresult))
    else:
        print ("Draw")"""
    s = string
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(s)):
        if s[i] in vowels:
         kevsc += (len(s)-i)
        else:
            stusc += (len(s)-i)

    if kevsc > stusc:
        print ("Kevin", kevsc)
    elif kevsc < stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")
