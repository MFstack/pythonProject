import re
f = open('students.txt')
print(f.readline())
pat = re.compile(r"\bd\w*r\b")
if pat.search('student.txt'):
    print("done")
