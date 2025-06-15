# CSI-Assignment---Week-2

# Singly Linked List in Python

This project provides a clean and efficient implementation of a *singly linked list* in Python using Object-Oriented Programming (OOP) principles. It includes key functionalities such as:

- Adding nodes to the end of the list
- Printing the list in readable format
- Deleting the Nth node (1-based index)
- Robust error handling for edge cases

---

## 📌 Features

- *Node Class*: Represents each element in the list with data and a next pointer.
- *LinkedList Class*:
  - add_node(data) – Adds a new node to the end.
  - delete_nth_node(n) – Deletes the node at position n (1-based).
  - print_list() – Displays all nodes in the list.
- *Exception Handling*:
  - Graceful handling of deletion from an empty list.
  - Validates the index for out-of-range operations.
  - Descriptive error messages to assist debugging.

---

## 🚀 How to Run

1. Clone the repository or download the code file.
2. Make sure you have Python 3 installed.
3. Run the script from your terminal:

```bash
python Linked_list.py
```
---


## 🧪 Sample Output
```bash
Adding elements to the list:

Adding: 10
Adding: 20
Adding: 30
Adding: 40
Adding: 50

Current List:
Linked List: 10 -> 20 -> 30 -> 40 -> 50

Deleting 3rd node:
Deleted node at position 3 with value '30'
Linked List: 10 -> 20 -> 40 -> 50

Deleting 1st node:
Deleted node at position 1 with value '10'
Linked List: 20 -> 40 -> 50

Attempting to delete 10th node :
Error: Index 10 is out of range for the current list.
```
---

## 📚 Learning Outcome

This project demonstrates practical understanding of:

•	Building a custom data structure in Python

•	Managing memory using linked nodes

•	Implementing safe deletion and traversal

•	Applying exception handling to ensure code robustness

---




