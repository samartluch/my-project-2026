students=[
{"name": "Sok", "score": 85},
{"name": "Dara", "score": 42},
{"name": "Rith", "score": 73},
{"name": "Sophy", "score": 35},
{"name": "Mony", "score": 90},
]
# Q1
for student in students:
    print(f"name: {student['name']}, Score: {student['score']}")
    Q2
for student in students:
    if student['score']>50:
        print(student['name'])
        Q3
counter=0
for i in range(len(students)):
    if students[i]['score']<50:
        counter+=1
print(counter)
Q4
top = students[0]
for student in students:
    if student["score"] > top["score"]:
        top = student
print(top["name"], "with score", top["score"])
Q5
total = 0
for student in students:
    total += student["score"]

average = total / len(students)
print("Average score:", average)
Q6
search_name = "Rith"
for student in students:
    if student["name"] == search_name:
        print(f"{search_name}'s score is {student['score']}")
 Q7
found = False
for student in students:
    if student["name"] == search_name:
        print(f"{student['name']}'s score is {student['score']}")
        found = True
        break

if not found:
    print(f"{search_name} not found.")
for i in range(len(students)):
    for j in range(i + 1, len(students)):
        if students[j]["score"] > students[i]["score"]:
            # ប្ដូរទីតាំង
            students[i], students[j] = students[j], students[i]

# បង្ហាញលំដាប់
for student in students:
    print(student["name"], student["score"])
Q8
for student in students:
    student["score"] += 5
    print(f"{student['name']}: {student['score']}")
Q9
remaining_students = []
for student in students:
    if student["score"] >= 40:
        remaining_students.append(student)
for student in remaining_students:
    print(student["name"])
Q10
scores = set()
duplicate_found = False

for student in students:
    if student["score"] in scores:
        duplicate_found = True
        break
    scores.add(student["score"])

if duplicate_found:
    print("There are duplicate scores.")
else:
    print("No duplicates")


