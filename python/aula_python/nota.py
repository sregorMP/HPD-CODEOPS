score = input("enter score")
score = int(score)
if score >= 80:
    grade = 'A'
else:
    if score >= 70:
        grade = 'B'
    else: 
        grade = 'C'
print("\n\n Grade is %s" % grade)