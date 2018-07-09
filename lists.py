n = int(input())
lists = []
for i in range(n):
    q = list(input().split())
    if(q[0] == 'print'):
        print (lists)
    elif(q[0] == 'reverse'):
        lists.reverse()   
    elif(q[0] == 'pop'):
        lists.pop()
    elif(q[0] == 'sort'):
        lists.sort()
    elif(q[0] == 'insert'):
        lists.insert(int(q[1]), int(q[2]))
    elif(q[0] == 'remove'):
        lists.remove(int(q[1]))
    else:
         lists.append(int(q[1]))
