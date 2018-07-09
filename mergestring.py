def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    parts = n//k
    t = []
    i = 0
    while(i < n):
        t.append(string[i:i+k])
        i = i + k
    for c in t:
        print("".join(sorted(set(c), key = c.index)))
            
