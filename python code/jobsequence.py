profit_list=[]
deadline_list=[]
jobs_list=[]
out_array_list=[]

    
def job_sequence(n,profit_list,deadline_list,max_deadline,jobs_list):
    u=max_deadline
    out_array_list=[0.0 for x in range(n)]
    for i in range(0,n):
        for j in range(deadline_list[i],-1,-1):
            if (out_array_list[j]==0.0):
                out_array_list[j]=jobs_list[i]
                break
    print("print output sequence:",out_array_list)



n=int(input("Enter number of jobs:"))
print("Enter profit :")
for i in range(0,n):
    item1=int(input())
    profit_list.append(item1)
print("Enter deadline :")
for i in range(0,n):
    item2=int(input())
    deadline_list.append(item2)
print("Enter  job_number:")
for i in range(0,n):
    item3=int(input())
    jobs_list.append(item3)
    
print("Entered profit:",profit_list)
print("Entered job deadline:",deadline_list)
print("Entered job number:",jobs_list)
max_deadline=deadline_list.index(max(deadline_list))
print("Maximum deadline is:", deadline_list[max_deadline])
job_sequence(n,profit_list,deadline_list,max_deadline,jobs_list)

