number_list=[]
def max_min(number_list,n):
    min_position=number_list.index(min(number_list))
    max_position=number_list.index(max(number_list))
    print("Minimum element in array at index:", number_list[min_position],min_position )
    print("Maximum element in array at index:", number_list[max_position],max_position )


n=int(input("Enter the number of element:"))
print("Enter the element:")
for i in range(0,n):
    item=int(input())
    number_list.append(item)
print("Entered elements are:",number_list)
max_min(number_list,n)
