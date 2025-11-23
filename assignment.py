# ============================
# Student Management System
# ============================

class StudentNode:
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        self.next = None


class StudentLinkedList:
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

    def delete_student(self, student_id):
        if not self.head:
            return

        if self.head.id == student_id:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next:
            if curr.next.id == student_id:
                curr.next = curr.next.next
                return
            curr = curr.next

    def search_student(self, student_id):
        curr = self.head
        while curr:
            if curr.id == student_id:
                return True
            curr = curr.next
        return False

    def show_students(self):
        if not self.head:
            return "No students"

        curr = self.head
        result = []
        i = 1
        while curr:
            result.append(f"{i}. {curr.name} (ID: {curr.id})")
            curr = curr.next
            i += 1
        return "\n".join(result)

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
