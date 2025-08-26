# CB 1st Average Grade
first_period = float(input(f"What is your grade in first period?"))
second_period = float(input(f"What is your grade in second period?"))
third_period = float(input(f"What is your grade in third period?"))
fourth_period = float(input(f"What is your grade in fourth period?"))
fifth_period = float(input(f"What is your grade in fifth period?"))
sixth_period = float(input(f"What is your grade in sixth period?"))
seventh_period = float(input(f"What is your grade in seventh period?"))

average_grade = (first_period + second_period + third_period + fourth_period + fifth_period + sixth_period + seventh_period)/7
average_grade = round(average_grade, 2)

print(f"Your average grade between all your classes is {str(average_grade)}%.")