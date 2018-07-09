f = open("abc.txt", "a+")
try:
    #f.write("Hello")
    print(f.read())
finally:
    f.close()
