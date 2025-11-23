class StudentNode:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name):
        pass

    def show_all(self):
        pass

    def search_student(self, student_id):
        pass

    def delete_student(self, student_id):
        pass

    def count_students(self):
        pass

    def update_student(self, student_id, new_name):
        pass
