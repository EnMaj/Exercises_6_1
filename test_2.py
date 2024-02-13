"""n = int(input())
count_courses = 0
for i in range(n):
    courses = input()
    if courses!="":
        count_courses+=courses.count(" ") + 1

print(count_courses)"""

n = int(input())
courses = set()
for i in range(n):
    courses.update(set(map(str, input().split(" "))))
print(len(courses))
