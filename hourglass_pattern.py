arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

sumslist = []

def calculatesum(i,j):
    return(arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + a[i+2][j+1] + a[i+2][j+2])

for j in range(0,4):
    for i in range(0,4):
        sum = calculatesum(i,j)
        sumslist.append(sum)
    
print(max(sumslist))