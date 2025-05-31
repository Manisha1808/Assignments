class Node:
    """A node in a singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to manage the singly linked list"""
    def __init__(self):
        self.head = None

    def add_node(self, data):
        """Add a node at the end of the list"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            print(f"Added head node: {data}")
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        print(f"Added node: {data}")

    def print_list(self):
        """Print the list"""
        if not self.head:
            print("List is empty.")
            return
        current = self.head
        print("Linked List: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index)"""
        try:
            if not self.head:
                raise Exception("Cannot delete from an empty list.")
            if n <= 0:
                raise IndexError("Index must be a positive integer.")

            if n == 1:
                deleted_value = self.head.data
                self.head = self.head.next
                print(f"Deleted node at position 1 with value: {deleted_value}")
                return

            current = self.head
            for i in range(n - 2):
                if current.next is None:
                    raise IndexError("Index out of range.")
                current = current.next

            if current.next is None:
                raise IndexError("Index out of range.")

            deleted_value = current.next.data
            current.next = current.next.next
            print(f"Deleted node at position {n} with value: {deleted_value}")

        except Exception as e:
            print(f"Error: {e}")


# Testing the implementation

if __name__ == "__main__":
    ll = LinkedList()

    # Adding nodes
    ll.add_node(10)
    ll.add_node(20)
    ll.add_node(30)
    ll.add_node(40)
    ll.print_list()

    # Deleting the 2nd node
    ll.delete_nth_node(2)
    ll.print_list()

    # Deleting 1st node (head)
    ll.delete_nth_node(1)
    ll.print_list()

    # Deleting a node out of range
    ll.delete_nth_node(10)

    # Deleting remaining nodes
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    # Trying to delete from empty list
    ll.delete_nth_node(1)
