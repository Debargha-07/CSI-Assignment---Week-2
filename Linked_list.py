class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_nth_node(self, n):
        
        if n <= 0:
            raise IndexError("Index should be a positive integer starting from 1.")

        if not self.head:
            raise IndexError("Cannot delete from an empty list!!!!")

        if n == 1:
            deleted_data = self.head.data
            self.head = self.head.next
            print(f"Deleted node at position 1 with value '{deleted_data}'")
            return

        current = self.head
        prev = None
        count = 1

        while current and count < n:
            prev = current
            current = current.next
            count += 1

        if not current:
            raise IndexError(f"Index {n} is out of range for current list!!")

        prev.next = current.next
        print(f"Deleted node at position {n} with value '{current.data}'")

    def print_list(self):
       
        current = self.head
        if not current:
            print("The list is empty.")
            return

        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("Linked List:", " -> ".join(elements))


# Sample usage and testing
if __name__ == "__main__":
    my_list = LinkedList()

    print("Adding elements to the list:")
    for value in [10, 20, 30, 40, 50]:
        print(f"Adding: {value}")
        my_list.add_node(value)

    print("\nCurrent List:")
    my_list.print_list()

    try:
        print("\nDeleting 3rd node:")
        my_list.delete_nth_node(3)
        my_list.print_list()

        print("\nDeleting 1st node:")
        my_list.delete_nth_node(1)
        my_list.print_list()

        print("\nAttempting to delete 10th node :")
        my_list.delete_nth_node(10)

    except IndexError as e:
        print(f"Error: {e}")