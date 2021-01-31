#School adminstration program
import csv
def write_csv(list_info):
    with open("student.csv",'a',newline='') as csv_file:
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow(["S.No","Name","D.O.B","Student I.D No.","Contact number","Email I.D"])
        writer.writerow(list_info)
condition=True
i_d=1
while(condition):
    student_info=input("Please enter the details of the Student {} in the following format(name, D.O.B(DD/MM/YYYY), Student I.D No.,contact number,email I.d )\n".format(i_d))
    student_info_list=student_info.split(" ")
    print("\nThe entered information is: \nName: {}\nD.O.B: {}\nStudent I.D No.: {}\nContact number: {}\nEmail I.D: {}" \
    .format(student_info_list[0], student_info_list[1],student_info_list[2],student_info_list[3],student_info_list[4]))
    choice_check=input("Is the entered information correct?(yes/no)")
    if choice_check=="yes":
        student_info_list.insert(0,i_d)
        write_csv(student_info_list)

        condition_check=input("Do you want to enter information for another student? (yes/no)")
        if condition_check=="yes":
            condition=True
            i_d=i_d+1
        elif condition_check=="no":
            condition=False
    elif choice_check=="no":
        print("\nPlease renter the values")
