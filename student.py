students_db = {}
def add_student(student_id, name, age, grade, email, department, city, phone):
    if not student_id:
        return "Invalid ID"
    if "@" not in str(email):
        return "Invalid Email Format"
    students_db[student_id] = {
        "name": name,
        "age": age,
        "grade": grade,
        "email": email,
        "department": department,
        "city": city,
        "phone": phone
    }
    return "Student added successfully"
def remove_student(student_id):
    if student_id in students_db:
        del students_db[student_id]
        return "Student removed successfully"
    return "Student not found"
def search_student(student_id):
    clean_id = str(student_id).strip()
    return students_db.get(clean_id, "Student not found")
def update_student(student_id, name=None, age=None, grade=None, email=None, department=None, city=None, phone=None):
    """Updates an existing student's information explicitly by matching parameters."""
    if student_id in students_db:
        if name is not None:
            students_db[student_id]["name"] = name
        if age is not None:
            students_db[student_id]["age"] = age
        if grade is not None:
            students_db[student_id]["grade"] = grade
        if email is not None:
            students_db[student_id]["email"] = email
        if department is not None:
            students_db[student_id]["department"] = department
        if city is not None:
            students_db[student_id]["city"] = city
        if phone is not None:
            students_db[student_id]["phone"] = phone
        return "Student updated successfully"
    return "Student not found"