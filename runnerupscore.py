if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
arr = list(dict.fromkeys(arr))
print(arr)
print(arr.sort())
print(arr.reverse())
print(arr[1])

