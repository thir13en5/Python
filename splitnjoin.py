def split_and_join(line):
    # write your code here
    s1 = ''
    l = list(line.split())
    for i in range(len(l)-1):
        s1 = s1 + l[i] + '-'
    s1 = s1 + l[len(l)-1]
    return s1
