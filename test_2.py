"""n = int(input())
count_courses = 0
for i in range(n):
    courses = input()
    if courses!="":
        count_courses+=courses.count(" ") + 1

print(count_courses)"""

n = int(input())
courses = []
for i in range(n):
    courses_student = list(map(str, input().split(" ")))
    courses+=courses_student
courses = set(courses)
print(len(courses))
