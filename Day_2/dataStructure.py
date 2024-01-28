my_list = list(["ad","ak","fz"])

list_env= ["add","sub","mut"]


print((list_env.append("jai ho")))
(my_list.append("jai hoooo"))
# print(my_list)


list_env.insert(1,"testing")
list_env.reverse()
list_env.extend("aditya")
list_env.sort()

# print(list_env)


obj ={
    "name":"aditya",
    "class":12,
    "number":321233,
    "active":True
}


obj_1 ={
    "name":"ak",
    "class":12,
    "number":321233,
    "active":True
}


obj_2 ={
    "name":"ad",
    "class":12,
    "number":321233,
    "active":False
}

result = [obj,obj_1,obj_2]

for i  in result:
    for  key,values in i.items():
        if key == "active" and values == True:
            print(i)

    
