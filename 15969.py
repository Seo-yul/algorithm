N = input()
student_score = list(map(int, input().split(' ')))

print(max(student_score)-min(student_score))