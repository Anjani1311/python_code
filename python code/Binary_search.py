number_list=[]
def is_array_sorted(number_list,n):
    a=1
    b=1
    i=0
    while ((a==1 or b==1) and i<n-1):
        if(number_list[i]<number_list[i+1]):
            b=0
        elif (number_list[i]>number_list[i+1]):
            a=0
        i=i+1
    if(a==1):
        return 0
    elif(b==1):
        return 1
    else:
        print("You have entered wrong order.")

def Desending_order(number_list,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if(number_list[i]<number_list[j]):
                temp=number_list[i]
                number_list[i]=number_list[j]
                number_list[j]=temp
    print("Desending order:",number_list)

def Ascending_order(number_list,n):
    for i in range(0,n):
        for j in range(i+1,n):
            if(number_list[i]>number_list[j]):
                temp=number_list[i]
                number_list[i]=number_list[j]
                number_list[j]=temp
    print("Ascending order:",number_list)

def binary_search(number_list,first,last,key,n):
    check=is_array_sorted(number_list,n)
    while(first<last):
        middle=(first+last)//2
        if(check==0):
            if(number_list[middle]==key):
                print("Element is present at index :",middle)
                break
            elif (number_list[middle]<key):
                first=middle+1
            else:
                last=middle-1
        elif(check==1):
            if(number_list[middle]==key):
                print("Element is present at index :",middle)
                break
            elif (number_list[middle]>key):
                first=middle+1
            else:
                last=middle-1
    if(first>last):
        print("Element is not found in array.")
            


    
n=int(input("Enter the number of element:"))
print("Enter the element:")
for i in range(0,n):
    item=int(input())
    number_list.append(item)
print("Entered elements are:",number_list)
is_array_sorted(number_list,n)
first=0
last=n-1
key=int(input("Enter searching element:"))
order=int(input("For Assending order press '1' and for Desending order press '0' :"))
if(order==0):
    Desending_order(number_list,n)
    binary_search(number_list,first,last,key,n)
elif(order==1):
    Ascending_order(number_list,n)
    binary_search(number_list,first,last,key,n)
else:
    print("you have enter wrong input.")
    
    
