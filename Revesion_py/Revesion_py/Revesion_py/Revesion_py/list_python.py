marks = 400

if marks >= 101:
    print("Please verify your grade again")
    exit()

if marks >=90:
    grade ="A"

if marks >=80:
    grade ="B"

if marks >=60:
    grade ="c"

if marks >=50:
    grade ="D"

else: 
    grade ="fail"

print("Grade",grade)