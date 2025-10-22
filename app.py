from flask import Flask

app = Flask('app')

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

@app.route("/old_students/", methods=["GET"])
def old_students():
    old_studs = []
    for student in students:
        if student['age'] > 20:
            old_studs.append(student)
    return old_studs

@app.route("/young_students/", methods=["GET"])
def young_students():
    young_studs = []
    for student in students:
        if student['age'] < 21:
            young_studs.append(student)
    return young_studs

@app.route("/advance_students/", methods=["GET"])
def advance_students():
    adv_stud = []
    for student in students:
        if student['age'] < 21 and student['grade'].upper() == 'A':
            adv_stud.append(student)
    return (adv_stud)

@app.route("/student_names", methods=["GET"])
def student_names():
    name_list = []
    for student in students:
        name_list.append({"First Name": student['first_name'], "Last Name": student['last_name']})
    return (name_list)
@app.route("/student_ages", methods=["GET"])
def student_ages():
    age_list = []
    for student in students:
        age_list.append({"Student name": student['first_name']+ " " + student['last_name'], "Age": student['age']})
    return age_list

@app.route("/students/", methods=["GET"])
def studs():
    studs = []
    for student in students:
        studs.append(student)
    return studs

app.run(debug=True, port=8000)