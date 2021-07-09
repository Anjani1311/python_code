weight_list=[]
price_list=[]

def knapsack(capacity,weight_list,price_list):
    x=list(range(len(price_list)))
    ratio=[v/w for v,w in zip(price_list,weight_list)]
    x.sort(key=lambda i:ratio[i],reverse=True)
    Maximum_profit=0
    for i in x:
        if(weight_list[i]<=capacity):
            Maximum_profit+=price_list[i]
            capacity-=weight_list[i]
        else:
            Maximum_profit+=(price_list[i]*capacity)/weight_list[i]
            break
    return Maximum_profit
    
n=int(input("Enter how many number of object available in market:"))
print("Enter weight of object:")
for i in range(0,n):
    item1=int(input())
    weight_list.append(item1)
print("Enter price:")
for i in range(0,n):
    item2=int(input())
    price_list.append(item2)
print("Entered profit:",weight_list)
print("Entered price list of objects:",price_list)
capacity=int(input("Enter capacity of the bag:"))
Maximum_profit=knapsack(capacity,weight_list,price_list)
print("Maximum profit obtaind:",Maximum_profit)
