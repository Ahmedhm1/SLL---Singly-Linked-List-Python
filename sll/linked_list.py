"""
Singly Linked List implementation in Python.

This module provides two classes:
1. Node: Represents a node in the singly linked list.
2. LinkedList: Represents the linked list with operations:
   - Append values at the end
   - Insert values at a specific index
   - Remove from beginning, end, by value, or by index
   - Reverse the list
   - Change a value at a given index
   - Check if the list is empty
   - String representation of the list

Author: [Ahmed Hisham]
License: MIT
"""


class Node:
    """
    Represents a single node in the singly linked list.

    Attributes:
        Value (any): The value stored in the node.
        next (Node): Reference to the next node in the list.
    """
    def __init__(self, Value):
        self.Value = Value
        self.next = None


class LinkedList:
    """
    Singly Linked List (SLL) implementation.

    Attributes:
        head (Node): The first node in the list.
        tail (Node): The last node in the list.
        items (int): The number of nodes in the list.
    """
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
        self.tail = None
        self.items = 0

    def append(self, value):
        """
        Insert a value at the end of the list.

        Args:
            value (any): The value to insert.

        Returns:
            True if inserted successfully.
        """
        new_node = Node(value)

        if not self.head:  # List is empty
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.items += 1
        return True

    def __str__(self):
        """
        Get a string representation of the list.

        Returns:
            str: Values joined by " -> " arrows.

        Raises:
            Exception: If the list is empty.
        """
        if not self.head:
            raise Exception("List is empty")

        current_node = self.head
        values = []
        while current_node:
            values.append(str(current_node.Value))
            current_node = current_node.next
        return " -> ".join(values)

    def insert(self, Value, index):
        """
        Insert a value at a specific index.

        Args:
            Value (any): Value to insert.
            index (int): Position to insert at (0-based).

        Returns:
            True if inserted successfully.

        Raises:
            Exception: If index is invalid.
        """
        if index < 0 or index > self.items:
            raise Exception("Invalid Index")

        new_node = Node(Value)
        self.items += 1

        if index == 0:  # Insert at beginning
            new_node.next = self.head
            self.head = new_node
            if not self.tail:  # List was empty
                self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next

            new_node.next = current_node.next
            current_node.next = new_node

            if new_node.next is None:  # Inserted at end
                self.tail = new_node

        return True

    def pop(self):
        """
        Remove the last element from the list.

        Returns:
            The value of the removed node.

        Raises:
            Exception: If the list is empty.
        """
        if not self.head:
            raise Exception("List is empty")

        if self.items == 1:  # Only one element
            pop_node = self.tail
            self.head = self.tail = None
            self.items -= 1
            return pop_node.Value

        current_node = self.head
        while current_node.next != self.tail:
            current_node = current_node.next

        pop_node = self.tail
        self.tail = current_node
        current_node.next = None
        self.items -= 1
        return pop_node.Value

    def change_value(self, Value, index):
        """
        Change the value at a specific index.

        Args:
            Value (any): The new value.
            index (int): Position of the node to update.

        Returns:
            True if updated successfully.

        Raises:
            Exception: If the list is empty or index is invalid.
        """
        if not self.head:
            raise Exception("List is empty")

        if index < 0 or index >= self.items:
            raise Exception("Invalid Index")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        current_node.Value = Value
        return True

    def is_empty(self):
        """
        Check if the list is empty.

        Returns:
            True if empty, False otherwise.
        """
        return self.items == 0

    def delete_front(self):
        """
        Remove the first element from the list.

        Returns:
            The removed value.

        Raises:
            Exception: If the list is empty.
        """
        if self.is_empty():
            raise Exception("List is empty")

        current = self.head
        if self.items == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            current.next = None

        self.items -= 1
        return current.Value

    def delete_value(self, value):
        """
        Remove a node by value.

        Args:
            value (any): The value to remove.

        Returns:
            The removed value if found, -1 otherwise.

        Raises:
            Exception: If the list is empty.
        """
        if self.is_empty():
            raise Exception("List is empty")

        if self.head.Value == value:
            return self.delete_front()
        if self.tail.Value == value:
            return self.pop()

        current_node = self.head.next
        prev_node = self.head
        while current_node and current_node.Value != value:
            prev_node = current_node
            current_node = current_node.next

        if current_node and current_node.Value == value:
            prev_node.next = current_node.next
            self.items -= 1
            return value
        else:
            return -1

    def delete_index(self, index):
        """
        Remove a node by index.

        Args:
            index (int): The index of the node to remove.

        Returns:
            The removed value if found, True otherwise.

        Raises:
            Exception: If list is empty or index is invalid.
        """
        if index < 0 or index >= self.items:
            raise Exception("Invalid Index")

        if self.is_empty():
            raise Exception("List is empty")

        if index == 0:
            return self.delete_front()
        elif index == (self.items - 1):
            return self.pop()

        current_node = self.head.next
        prev_node = self.head
        i = 1
        while current_node and i != index:
            current_node = current_node.next
            prev_node = prev_node.next
            i += 1

        if i == index:
            prev_node.next = current_node.next
            self.items -= 1
            return True
        else:
            return -1

    def reverse(self):
        """
        Reverse the entire list in-place.

        Returns:
            True if reversed successfully.
        """
        if self.is_empty():
            raise Exception("List is empty")
        if self.items == 1:
            return True

        prev = None
        curr = self.head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.tail = self.head
        self.head = prev
        return True
