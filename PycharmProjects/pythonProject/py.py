

students = {
   "+1": ['', 18 ,True],
  "+22": ['Adell', 12 ,True],
  "+30": ['', 34 ,False],
 }

  if "+55" in students:
     students.pop("+55")
  else:
print("none")

print(students) students.items():
     if key==search:
         print(students[key])
     else:
print('there is no such a key')



print(students)



for key, value in students.items():
     print(key)
     print(value)



my_dict ={
     "name" : "Adelya",
     "age" : 18,
     "student" : True,
    "profession" : "Web Developer",
 },
{
print("name", my_dict["name"]),
print("age", my_dict["age"]),
print("student", my_dict["student"]),
print("profession", my_dict["profession"]),
 }

users = {
    "Tom": {
        "phone": "+971478745",
        "email": "tom12@gmail.com"
    },
    "Bob": {
        "phone": "+876390444",
        "email": "bob@gmail.com",
        "skype": "bob123"
    }
}


list_keys =[]
list_value=[]
for user,info in users.items():
    for key,value in info.items():
        list_keys.append(key)
        list_value.append(value)
print("Keys",list_keys)
print("Values",list_value)



my_list=[1,2,3]
my_list.extend([5])
print(my_list)


