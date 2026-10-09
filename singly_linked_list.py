# ============================================================
#           SINGLY LINKED LIST OPERATIONS IN PYTHON
# ============================================================


# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # 1. Create a linked list
    # --------------------------------------------------------
    def create_list(self):
        n = int(input("Enter the number of nodes: "))

        if n <= 0:
            print("The linked list is empty.")
            return

        for i in range(n):
            data = int(input(f"Enter data for node {i + 1}: "))
            self.add_end(data)

        print("Linked list created successfully!")

    # --------------------------------------------------------
    # 2. Add a node at the beginning
    # --------------------------------------------------------
    def add_begin(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

        print(f"{data} inserted at the beginning.")

    # --------------------------------------------------------
    # 3. Add a node at the end
    # --------------------------------------------------------
    def add_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

        print(f"{data} inserted at the end.")

    # --------------------------------------------------------
    # 4. Add a node at a specific position
    # Positions start from 1
    # --------------------------------------------------------
    def add_at_position(self, data, position):
        if position < 1:
            print("Invalid position!")
            return

        new_node = Node(data)

        # Insert at the beginning
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            print(f"{data} inserted at position {position}.")
            return

        temp = self.head
        current_position = 1

        while temp is not None and current_position < position - 1:
            temp = temp.next
            current_position += 1

        if temp is None:
            print("Invalid position!")
            return

        new_node.next = temp.next
        temp.next = new_node

        print(f"{data} inserted at position {position}.")

    # --------------------------------------------------------
    # 5. Delete the first node
    # --------------------------------------------------------
    def delete_begin(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        deleted_data = self.head.data
        self.head = self.head.next

        print(f"First node ({deleted_data}) deleted.")

    # --------------------------------------------------------
    # 6. Delete the last node
    # --------------------------------------------------------
    def delete_end(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        # Only one node exists
        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            print(f"Last node ({deleted_data}) deleted.")
            return

        temp = self.head

        while temp.next.next is not None:
            temp = temp.next

        deleted_data = temp.next.data
        temp.next = None

        print(f"Last node ({deleted_data}) deleted.")

    # --------------------------------------------------------
    # 7. Delete a node at a specific position
    # Positions start from 1
    # --------------------------------------------------------
    def delete_at_position(self, position):
        if self.head is None:
            print("Linked list is empty!")
            return

        if position < 1:
            print("Invalid position!")
            return

        # Delete the first node
        if position == 1:
            self.delete_begin()
            return

        temp = self.head
        current_position = 1

        while temp.next is not None and current_position < position - 1:
            temp = temp.next
            current_position += 1

        if temp.next is None:
            print("Invalid position!")
            return

        deleted_data = temp.next.data
        temp.next = temp.next.next

        print(
            f"Node containing {deleted_data} "
            f"at position {position} deleted."
        )

    # --------------------------------------------------------
    # 8. Reverse the linked list
    # --------------------------------------------------------
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next

            current.next = previous

            previous = current
            current = next_node

        self.head = previous

        print("Linked list reversed successfully!")

    # --------------------------------------------------------
    # 9. Delete the entire linked list
    # --------------------------------------------------------
    def delete_list(self):
        if self.head is None:
            print("Linked list is already empty!")
            return

        self.head = None

        print("Entire linked list deleted successfully!")

    # --------------------------------------------------------
    # Display the linked list
    # --------------------------------------------------------
    def display(self):
        if self.head is None:
            print("Linked list is empty!")
            return

        temp = self.head

        print("HEAD", end=" -> ")

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("NULL")


# ============================================================
#                    MAIN MENU
# ============================================================

def main():
    linked_list = SinglyLinkedList()

    while True:
        print("\n========== SINGLY LINKED LIST MENU ==========")
        print("1.  Create a linked list")
        print("2.  Add a node at the beginning")
        print("3.  Add a node at the end")
        print("4.  Add a node at a specific position")
        print("5.  Delete the first node")
        print("6.  Delete the last node")
        print("7.  Delete a node at a specific position")
        print("8.  Reverse the linked list")
        print("9.  Delete the entire linked list")
        print("10. Display the linked list")
        print("11. Exit")
        print("=============================================")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                linked_list.create_list()

            elif choice == 2:
                data = int(input("Enter the data: "))
                linked_list.add_begin(data)

            elif choice == 3:
                data = int(input("Enter the data: "))
                linked_list.add_end(data)

            elif choice == 4:
                data = int(input("Enter the data: "))
                position = int(input("Enter the position: "))
                linked_list.add_at_position(data, position)

            elif choice == 5:
                linked_list.delete_begin()

            elif choice == 6:
                linked_list.delete_end()

            elif choice == 7:
                position = int(input("Enter the position: "))
                linked_list.delete_at_position(position)

            elif choice == 8:
                linked_list.reverse()

            elif choice == 9:
                linked_list.delete_list()

            elif choice == 10:
                linked_list.display()

            elif choice == 11:
                print("Program terminated successfully!")
                break

            else:
                print("Invalid choice! Please enter 1 to 11.")

        except ValueError:
            print("Invalid input! Please enter an integer.")


# Run the program
if __name__ == "__main__":
    main()