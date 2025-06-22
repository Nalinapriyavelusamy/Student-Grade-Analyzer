def student_report():
    name = input("Enter student name: ")
    
    m1 = int(input("English mark: "))
    m2 = int(input("Maths mark: "))
    m3 = int(input("Science mark: "))
    m4 = int(input("Social mark: "))
    m5 = int(input("Computer mark: "))

    total = m1 + m2 + m3 + m4 + m5
    average = total / 5

   
    if average >= 90:
        grade = 'A'
    elif average >= 75:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 40:
        grade = 'D'
    else:
        grade = 'Fail'

    
    print("\n STUDENT REPORT")
    print("------------------------")
    print("Name:", name)
    print("Total Marks:", total, "/ 500")
    print("Average:", round(average, 2))
    print("Grade:", grade)
    print("------------------------")


while True:
    student_report()
    again = input("Add another student? (yes/no): ")
    if again.lower() != "yes":
        break
