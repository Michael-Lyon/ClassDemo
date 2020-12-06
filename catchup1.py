#dictionaries
all_student = {}
new_student = {
      "name":"Jane",
      "surname":"Abu",
      "class":"Python",
      "sport":"VolleyBall",
      "music":"dance"
}

print(new_student['name'])
for key in new_student:
    # print(f"{key} ===> {new_student[key]}")
    pass

for key, value in new_student.items():
    # print(key, value)
    pass

new_student['music'] = "Electronic"
print(new_student['music'])

new_student.update({'color':'black'})
print(new_student)

empty = new_student.copy()