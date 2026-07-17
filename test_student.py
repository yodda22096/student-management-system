import pytest
from student import add_student, remove_student, search_student, update_student, students_db
@pytest.fixture(autouse=True)
def setup_10_students():
    students_db.clear()
    add_student("S01", "Sania", 21, "A", "sania@example.com", "Cyber Security", "Mumbai", "9876543210")
    add_student("S02", "Amit", 22, "B", "amit@example.com", "Data Science", "Bangalore", "9876543211")
    add_student("S03", "Priya", 20, "A", "priya@example.com", "Machine Learning", "Pune", "9876543212")
    add_student("S04", "Rahul", 23, "C", "rahul@example.com", "Information Technology", "Delhi", "9876543213")
    add_student("S05", "Neha", 21, "B", "neha@example.com", "Cyber Security", "Mumbai", "9876543214")
    add_student("S06", "Vikram", 22, "A", "vikram@example.com", "Data Science", "Chennai", "9876543215")
    add_student("S07", "Rohan", 20, "B", "rohan@example.com", "Digital Forensics", "Hyderabad", "9876543216")
    add_student("S08", "Anjali", 21, "A", "anjali@example.com", "Machine Learning", "Mumbai", "9876543217")
    add_student("S09", "Kabir", 24, "C", "kabir@example.com", "Information Technology", "Kolkata", "9876543218")
    add_student("S10", "Simran", 22, "A", "simran@example.com", "Cyber Security", "Bangalore", "9876543219")
    yield

# 1. Verify database initialization size
def test_database_has_10_records():
    assert len(students_db) == 10
# 2. Validate column structure of a specific student record
def test_student_column_structure():
    student = search_student("S01")
    expected_columns = ["name", "age", "grade", "email", "department", "city", "phone"]
    for col in expected_columns:
        assert col in student

# 3. Validate column content matching
def test_student_data_accuracy():
    student = search_student("S03")
    assert student["name"] == "Priya"
    assert student["department"] == "Machine Learning"
    assert student["city"] == "Pune"

# 4. Input validation: Empty ID check
def test_add_student_validation_empty_id():
    res = add_student("", "Raj", 22, "A", "raj@example.com", "CS", "Mumbai", "9999999999")
    assert res == "Invalid ID"

# 5. Input validation: Bad email check
def test_add_student_validation_bad_email():
    res = add_student("S11", "Raj", 22, "A", "raj_at_example.com", "CS", "Mumbai", "9999999999")
    assert res == "Invalid Email Format"

# 6. Search validation for missing records
def test_search_non_existent_student():
    assert search_student("S999") == "Student not found"

# 7. Update validation for specific column modifications
def test_update_student_specific_columns():
    res = update_student("S01", city="Navi Mumbai", grade="A+")
    assert res == "Student updated successfully"
    assert students_db["S01"]["city"] == "Navi Mumbai"
    assert students_db["S01"]["grade"] == "A+"

# 8. Update validation for non-existent student
def test_update_non_existent_student():
    res = update_student("S999", city="New City")
    assert res == "Student not found"

# 9. Removal validation check
def test_remove_student_validation():
    res = remove_student("S02")
    assert res == "Student removed successfully"
    assert "S02" not in students_db
    assert len(students_db) == 9

# 10. Core Search edge-case handling (Whitespace trimming validation)
def test_search_student_with_spaces():
    # Pass ID with spacing to ensure search handles clean inputs seamlessly
    assert search_student("  S05  ")["name"] == "Neha"