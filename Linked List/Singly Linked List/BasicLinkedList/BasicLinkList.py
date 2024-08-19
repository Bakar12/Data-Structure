class Node:
    def __init__(self, data):
        self.data = data  # Store the data
        self.next = None  # Pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node
        new_node.next = self.head  # Point the new node to the current head
        self.head = new_node  # Update the head to the new node

    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node  # Set the new node as the head
            return
        last = self.head
        while last.next:  # Traverse to the end of the list
            last = last.next
        last.next = new_node  # Point the last node to the new node

    def insert_at_position(self, position, data):
        if position == 0:  # If inserting at the beginning
            self.insert_at_beginning(data)
            return
        new_node = Node(data)  # Create a new node
        current = self.head
        for _ in range(position - 1):  # Traverse to the position
            if not current:
                raise IndexError("Position out of bounds")
            current = current.next
        new_node.next = current.next  # Point the new node to the next node
        current.next = new_node  # Point the current node to the new node

    def delete_by_value(self, value):
        current = self.head
        if current and current.data == value:  # If the head needs to be deleted
            self.head = current.next  # Update the head
            current = None
            return
        prev = None
        while current and current.data != value:  # Traverse to find the node
            prev = current
            current = current.next
        if not current:  # If the value is not found
            return
        prev.next = current.next  # Point the previous node to the next node
        current = None  # Delete the current node

    def delete_by_position(self, position):
        if not self.head:  # If the list is empty
            return
        current = self.head
        if position == 0:  # If the head needs to be deleted
            self.head = current.next  # Update the head
            current = None
            return
        for _ in range(position - 1):  # Traverse to the position
            if not current:
                raise IndexError("Position out of bounds")
            current = current.next
        if not current or not current.next:  # If the position is out of bounds
            raise IndexError("Position out of bounds")
        next_node = current.next.next  # Point to the node after the next node
        current.next = None  # Delete the next node
        current.next = next_node  # Update the current node's next pointer

    def search(self, value):
        current = self.head
        while current:  # Traverse the list
            if current.data == value:  # If the value is found
                return True
            current = current.next
        return False  # If the value is not found

    def display(self):
        current = self.head
        while current:  # Traverse the list
            print(current.data, end=" -> ")  # Print the data
            current = current.next
        print("None")  # Indicate the end of the list


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_beginning(0)
    ll.insert_at_position(2, 1.5)
    ll.display()  # Output: 0 -> 1 -> 1.5 -> 2 -> 3 -> None

    ll.delete_by_value(1.5)
    ll.display()  # Output: 0 -> 1 -> 2 -> 3 -> None

    ll.delete_by_position(0)
    ll.display()  # Output: 1 -> 2 -> 3 -> None

    print(ll.search(2))  # Output: True
    print(ll.search(4))  # Output: False
