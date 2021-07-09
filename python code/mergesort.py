number_list=[]
def merge(number_list,lb,mid,ub):
    left=number_list[lb:mid+1]
    right=number_list[mid+1:ub+1]
    i=0
    j=0
    k=lb
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            number_list[k]=left[i]
            i=i+1
        else:
            number_list[k]=right[j]
            j=j+1
        k=k+1
    while j<len(right):
        number_list[k]=right[j]
        j=j+1
        k=k+1
    while i<len(left):
        number_list[k]=left[i]
        i=i+1
        k=k+1
def merge_sort(number_list,lb,ub):
    if lb<ub:
        mid=(lb+ub)//2
        merge_sort(number_list,lb,mid)
        merge_sort(number_list,mid+1,ub)
        merge(number_list,lb,mid,ub)
n=int(input("Enter the number of element:"))
print("Enter the element:")
for i in range(0,n):
    item=int(input())
    number_list.append(item)
print("Before sorting elements are:",number_list)
lb=0
ub=n-1
merge_sort(number_list,lb,ub)
print("After sorting elements are:",number_list)


