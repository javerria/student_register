'''Gets input about student IDs and creates a sign-in sheet'''

#Ask user for number of students
count = int((input("How many students do you want to register? ")))

#Define list to store all student IDs entered
all_IDs = []

#Run the loop enough times to iterate through the number of students wanted
current = 1
while current <= count:
    #Enter student ID and store in variable
    student_ID = (input(f"Please enter student ID #{current}: "))
    #Add to list defined earlier
    all_IDs.append(student_ID)
    #Move on to next student
    current += 1

#Open the file in append mode
with open ("reg_form.txt", 'a') as file:
    file.write("STUDENT REGISTRATION FORM\n")
    #Write to the file for each element in the list of student IDs
    for ID in all_IDs:
        file.write(ID + "...........................\n")

print("Student registration form has been created under filename \'reg_form.txt\'")
