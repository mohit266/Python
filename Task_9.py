def miniMaxSum(arr):
    sum=0
    for i in range(len(arr)):
        sum = sum + arr[i]
        print(sum)
    print(sum-max(arr), sum-min(arr))

if __name__ == '__main__':
    miniMaxSum([7, 69, 2, 221, 8974])