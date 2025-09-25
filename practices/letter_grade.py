# CB 1st Letter Grade
global classes
global num_grades
global gp_list
global letter_grades
classes = []
num_grades = []
gp_list = []
letter_grades = []
index_count = -1

def percent_translation(grade,class_name):
    if grade >= 94 and grade <= 100:
        print(f"You have an A in {class_name}. That is equal to a 4.0 on the regular GPA scale.")
        letter_grades.append("A")
        gp_list.append(4.0)
        return True
    elif grade >= 90 and grade <= 93:
        print(f"You have an A- in {class_name}. That is equal to a 3.7 on the regular GPA scale.")
        letter_grades.append("A-")
        gp_list.append(3.7)
        return True
    elif grade >= 87 and grade <= 89:
        print(f"You have an B+ in {class_name}. That is equal to a 3.3 on the regular GPA scale.")
        letter_grades.append("B+")
        gp_list.append(3.3)
        return True
    elif grade >= 84 and grade <= 86:
        print(f"You have an B in {class_name}. That is equal to a 3.0 on the regular GPA scale.")
        letter_grades.append("B")
        gp_list.append(3.0)
        return True
    elif grade >= 80 and grade <= 93:
        print(f"You have an B- in {class_name}. That is equal to a 2.7 on the regular GPA scale.")
        letter_grades.append("B-")
        gp_list.append(2.7)
        return True
    elif grade >= 77 and grade <= 79:
        print(f"You have an C+ in {class_name}. That is equal to a 2.3 on the regular GPA scale.")
        letter_grades.append("C+")
        gp_list.append(2.3)
        return True
    elif grade >= 74 and grade <= 76:
        print(f"You have an C in {class_name}. That is equal to a 2.0 on the regular GPA scale.")
        letter_grades.append("C")
        gp_list.append(2.0)
        return True
    elif grade >= 70 and grade <= 73:
        print(f"You have an C- in {class_name}. That is equal to a 1.7 on the regular GPA scale.")
        letter_grades.append("C-")
        gp_list.append(1.7)
        return True
    elif grade >= 65 and grade <= 69:
        print(f"You have an D in {class_name}. That is equal to a 1.0 on the regular GPA scale.")
        letter_grades.append("D")
        gp_list.append(1.0)
        return True
    elif grade >= 60 and grade <= 64:
        print(f"You have an D- in {class_name}. That is equal to a 0.7 on the regular GPA scale.")
        letter_grades.append("D-")
        gp_list.append(0.7)
        return True
    elif grade < 60:
        print(f"You have an F in {class_name}. That is equal to a 0.0 on the regular GPA scale.")
        letter_grades.append("A")
        gp_list.append(0)
        return True
    else:
        print("invalid grade entered")
        return False


while True:
    class_name = input("What class are you taking?").strip()
    if class_name in classes:
        print("Class has already been inputted.")
        continue
    else:
        classes.append(class_name)
        index_count += 1
        while True:
            grade = input(f"What grade do you have in {class_name}? Do not include the percent sign.").strip()
            if grade.isalpha() or float(grade) > 100 or float(grade) < 0:
                print("invalid answer")
                continue
            else:
                grade = float(grade)
                break
        num_grades.append(grade)
        percent_translation(grade,class_name)
        if percent_translation == False:
            continue
        else:
            while True:
                grades_total = sum(num_grades)
                gp_total = sum(gp_list)
                average_grade = grades_total/len(num_grades)
                rounded_average = round(average_grade,2)
                gpa = gp_total/len(gp_list)
                print(f"Letter grade for {class_name}: {letter_grades[index_count]}\n Grade Point Score for {classes[index_count]}: {gp_list[index_count]} ")
                print(f"Average grade: {rounded_average}\n GPA: {gpa}")
                break
            repeat = input("Do you want to input another grade? Yes/No").strip().capitalize()
            if repeat == "Yes":
                continue
            elif repeat == "No":
                print("Goodbye!")
                break
            else:
                print("invalid answer; goodbye!")
                break