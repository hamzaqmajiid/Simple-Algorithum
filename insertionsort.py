lst=[12,45,72,98,58,6,3,58,100,12,34]
print(lst)
for i in range(1,len(lst)):
    key=lst[i]
    j=i-1
    while j>=0 and key<lst[j]:
        lst[j+1]=lst[j]
        j-=1
    lst[j+1]=key
print("Sorted List")    
for i in range(len(lst)):
    print("%d"%lst[i])