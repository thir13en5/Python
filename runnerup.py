if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    arr1 = []
    max1 = max(arr)
    for i in arr:
        if(i != max1):
            arr1.append(i)
    max2 = max(arr1)
    print max2
