# Abstract Data Types 3

Abstract Data Types PDF:

https://drive.google.com/file/d/1jXGQdSvuUYjGXl-PUuHMUzKWEBGQoARL/view?usp=sharing


---

## Exercise 1

**Problem:**
 
**Student Management System (Linked List):**    
Implement a Student Management System **using Linked List**, not Python lists.

You will create:
- A `StudentNode` class. `StudentNode` contains `id` and `name`   
- A `StudentList` (Linked List) class    

Your linked list must support:   
1. **add_student(id, name)**    
   Insert at the *end* of the linked list.  
  
2. **delete_student(id)**    
   Remove the student with matching ID.    
   Return `True` if found & deleted, else `False`.  
    
3. **search_student(id)**    
   Return the student’s name if found, else `False`.  
  
4. **show_all()**    
   Return all students in this format:
   
       1 - Alice
       2 - Bob

Bonus points for:
1. `count_students()`:   
    Returns the total number of students currently in the linked list.    
       
2. `update_student(id, new_name)`:  
    Searches for a student by their id.   
    If found, updates the student's name to new_name.   
    

Example:

    Input:
       ll = StudentLinkedList()
       ll.add_student(1, "Alice")
       ll.add_student(2, "Bob")
       ll.add_student(3, "Charlie")
       ll.delete_student(2)
       print(ll.show_all())
    Output:
       1 - Alice
       3 - Charlie

      

---

