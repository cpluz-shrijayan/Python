if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr=list(arr)
    arr.sort(reverse=True)
    z=arr[0]
    while arr[0]==z:
        arr.remove(z)
    print(arr[0])
