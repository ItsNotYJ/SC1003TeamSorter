import random
import copy

#V3 read the file manually
with open("students.csv", "r") as file:
    lines = file.read().strip().split("\n")
                                
#convert to 2d array
data = [line.split(",") for line in lines]

# separate header and rows
header = data[0]
rows = data[1:]

# Sort by Tutorial Group (first column, index 0)
sorted_rows = sorted(rows, key=lambda x: x[0])

#filtering out group 10 only
group_name = "G-10"
group_students = [row for row in rows if row [0] == group_name]

#finding the number of male and female students
Male_count = 0
Female_count = 0
Total_count = 0
Tutorial_Group = "G-10"

for row in sorted_rows:
    if row[0] == Tutorial_Group:
        if row[4] == "Male":
          Male_count += 1
        elif row[4] == "Female":
          Female_count += 1
    
Total_count = Male_count + Female_count
print("Number of male students:", Male_count)
print("Number of female students:", Female_count)
print("Number of total students:", Total_count)

#group size and parameter sorting
max_group_size = 5
max_faculty = 3
group = []
current_group = []
faculty_count = {}
faculty_index = 2
count = faculty_count.get(faculty, 0) #gets current dictionary count

for student in rows:
    faculty = student[faculty_index]

    if count < max_faculty:
        current_group.append(student)
        faculty_count[faculty] = count + 1
    else: #if faculty limited reached, start a new group
        group.append(current_group)
        current_group = [student]
        faculty_count = {faculty: 1}

    #if group is full, start a new one and reset count
    if len(current_group) == max_group_size:
        group.append(current_group)
        current_group = []
        faculty_counts = {}

#add any remaining students in the last group
if current_group:
    groups.append(current_group)

for index, group in enumerate(groups, start=1):
    print(f"\nGroup {idx}:")
    for student in group:
        print(student)

