list_of_names = list(["dev","stg","prd"]
)

list_OF_envs = ["dev","stg","prd"]
for i in list_OF_envs:
    print("Deploying to ")
    # print(i)


# print(dir(list_OF_envs))
    
    list_OF_envs.append("aditya")
    print(list_OF_envs)


list_of_num = [1,2,3,-2,-1,4,99,22,44,7]

for i in range(len(list_of_num)):
    for j in  range(len(list_of_num)):
        if list_of_num[i] > list_of_num[j]:
            ad=list_of_num[i]
            list_of_num[i] =list_of_num[j]
            list_of_num[j]=ad

print(list_of_num)


list_of_num = [1,2,3,-2,-1,4,99,22,44,7]

for i in range(len(list_of_num)):
    for j in  range(len(list_of_num)):
        if list_of_num[i] > list_of_num[j]:
            ad=list_of_num[i]
            list_of_num[i] =list_of_num[j]
            list_of_num[j]=ad

print(list_of_num)
        
        
