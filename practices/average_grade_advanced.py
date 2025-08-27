classes_total = input("How many classes are you taking? \n")
num_total = int(classes_total)
grades = []
global period
period = 0

for i in range(num_total):
    period += 1
    grade = input("What is your grade in period " + str(period) + "? Don't put a percent sign in your answer. \n")
    float_grade = float(grade)
    grades.append(float_grade)
    print(grades)

average_grade = (sum(grades))/num_total
rounded_average = round(average_grade, 2)
print(f"Your average grade is {str(rounded_average)}")

