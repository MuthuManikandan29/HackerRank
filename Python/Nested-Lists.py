# ========================
#       Information
# ========================

# Direct Link: https://www.hackerrank.com/challenges/nested-list/problem
# Difficulty: Easy
# Max Score: 10
# Language: Python

# ========================
#         Solution
# ========================



# Step 1: Read the number of students
n = int(input().strip())

# Step 2: Read the names and grades of each student
students = []
for _ in range(n):
    name = input().strip()
    grade = float(input().strip())
    students.append([name, grade])

# Step 3: Find the second lowest grade
grades = sorted(set([student[1] for student in students]))
second_lowest_grade = grades[1]

# Step 4: Identify all students who have the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Step 5: Sort the names of these students alphabetically
second_lowest_students.sort()

# Step 6: Print the names, each on a new line
for student in second_lowest_students:
    print(student)
