import pytest
from assignment import StudentList

@pytest.mark.parametrize("students, expected_output", [
    ([("101", "Alice"), ("102", "Bob")], "101 - Alice\n102 - Bob"),
    ([("200", "David")], "200 - David"),
])
def test_add_and_show(students, expected_output):
    sl = StudentList()
    for sid, name in students:
        sl.add_student(sid, name)
    assert sl.show_all().strip() == expected_output.strip()

@pytest.mark.parametrize("students, search_id, expected", [
    ([("101", "Alice")], "101", "Alice"),
    ([("1", "A"), ("2", "B"), ("3", "C")], "2", "B"),
])
def test_search(students, search_id, expected):
    sl = StudentList()
    for sid, name in students:
        sl.add_student(sid, name)
    assert sl.search_student(search_id) == expected

@pytest.mark.parametrize("students, delete_id, expected_result, expected_output", [
    ([("101", "Alice"), ("102", "Bob")], "101", True, "102 - Bob"),
    ([("1", "A"), ("2", "B"), ("3", "C")], "2", True, "1 - A\n3 - C"),
    ([("1", "A"), ("2", "B")], "2", True, "1 - A"),
    ([("1", "A")], "999", False, "1 - A"),

])
def test_delete(students, delete_id, expected_result, expected_output):
    sl = StudentList()
    for sid, name in students:
        sl.add_student(sid, name)

    result = sl.delete_student(delete_id)
    assert result == expected_result
    assert sl.show_all().strip() == expected_output.strip()

@pytest.mark.parametrize("students, expected_count", [
    ([], 0),
    ([("1", "A")], 1),
    ([("1", "A"), ("2", "B"), ("3", "C")], 3),
])
def test_count(students, expected_count):
    sl = StudentList()
    for sid, name in students:
        sl.add_student(sid, name)

    assert sl.count_students() == expected_count

@pytest.mark.parametrize("students, update_id, new_name, expected_result, expected_final", [
    ([("101", "Alice")], "101", "Alicia", True, "101 - Alicia"),
    ([("101", "Alice")], "999", "Ghost", False, "101 - Alice"),
    ([("1", "A"), ("2", "B"), ("3", "C")], "2", "Beta", True, "1 - A\n2 - Beta\n3 - C"),
])
def test_update(students, update_id, new_name, expected_result, expected_final):
    sl = StudentList()
    for sid, name in students:
        sl.add_student(sid, name)

    result = sl.update_student(update_id, new_name)
    assert result == expected_result
    assert sl.show_all().strip() == expected_final.strip()
