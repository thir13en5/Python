n = int(input())
dict1 = {}
for i in range(n):
    name, a, b, c, = input().split()
    dict1[name] = [float(a),float(b),float(c)]
query = input()
for key in dict1:
    if key == query:
        sum1  = sum(dict1[key])
        print ("%.2f" % (sum1/3))
