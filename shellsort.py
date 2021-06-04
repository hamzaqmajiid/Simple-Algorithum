arr = [ 12, 34, 54, 2, 3,8] 
n = len(arr)
gap =(int(n/2))

while gap > 0: 
    for i in range(int(n/2),n):
        temp = arr[i]
        j = i
        while  j >= int(n/2) and arr[j-int(n/2)] >temp:
            arr[j] = arr[j-gap]
            j -= int(n/2)
        arr[j] = temp
    gap /= 2

print ("Array after sorting:") 
for i in range(n): 
    print(arr[i])