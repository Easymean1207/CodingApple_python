students = [
    {"grade": "3", "name": "lee jimin", "dept": "CS"},
    {"grade": "2", "name": "hong gildong", "dept": "CE"},
    {"grade": "3", "name": "kim dongkwan", "dept": "CS"},
    {"grade": "1", "name": "Jetbrain", "dept": "SE"},
    {"grade": "2", "name": "Eclipse", "dept": "Swift"},
]

country = ["japan", "china", "korea", "taiwan", "russia"]

students.sort(key=lambda x: x["name"])
# print(students)
print(country)
