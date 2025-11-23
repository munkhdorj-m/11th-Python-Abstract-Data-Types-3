# ============================
# Student Management System
# ============================

class StudentNode:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.next = None


class StudentList:
    def __init__(self):
        self.head = None

    def add_student(self, student_id, name):
        new_node = StudentNode(student_id, name)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def show_all(self):
        if not self.head:
            return "No students found"
        curr = self.head
        result = []
        while curr:
            result.append(f"{curr.id} - {curr.name}")
            curr = curr.next
        return "\n".join(result)

    def search_student(self, student_id):
        curr = self.head
        while curr:
            if curr.id == student_id:
                return curr.name
            curr = curr.next
        return None

    def delete_student(self, student_id):
        if not self.head:
            return False
        if self.head.id == student_id:
            self.head = self.head.next
            return True
        curr = self.head
        while curr.next:
            if curr.next.id == student_id:
                curr.next = curr.next.next
                return True
            curr = curr.next
        return False

    def count_students(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def update_student(self, student_id, new_name):
        curr = self.head
        while curr:
            if curr.id == student_id:
                curr.name = new_name
                return True
            curr = curr.next
        return False
