class Student:
    def __init__(self, TG, student_id, faculty, name, gender, cgpa):
        self.TG = TG
        self.id = student_id
        self.faculty = faculty
        self.name = name
        self.gender = gender
        self.gpa = float(cgpa) 

    def __repr__(self):
        return f"Student({self.name}, {self.faculty}, {self.gpa})"


students = [Student(*row) for row in rows]

max_group_size = 5
max_faculty = 3
groups = []
current_group = []
faculty_count = {}

for student in students:
    faculty = student.faculty
    count = faculty_count.get(faculty, 0)

    if count < max_faculty:
        current_group.append(student)
        faculty_count[faculty] = count + 1
    else: #if faculty limited reached, start a new group
        groups.append(current_group)
        current_group = [student]
        faculty_count = {faculty: 1}

    #if group is full, start a new one and reset count
    if len(current_group) == max_group_size:
        groups.append(current_group)
        current_group = []
        faculty_count = {}

#add any remaining students in the last group
if current_group:
    groups.append(current_group)

for index, group in enumerate(groups, start=1):
    print(f"\nGroup {index}:")
    for student in group:
        print(student)
