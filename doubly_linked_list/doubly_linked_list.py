"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""

    def add_to_head(self, value):
        # Wrap the given value in a ListNode
        new_node = ListNode(value, None, None)  # """ No Next""" """ #No Prev """
        self.length += 1
        # If there is an existing list
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            # If there is no list
            self.head = new_node
            self.tail = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""

    def add_to_tail(self, value):
        # Wrap the given value in a ListNode
        new_node = ListNode(value, None, None)  # """ No Next""" """ #No Prev """
        self.length += 1
        # If there is an existing list
        if self.tail is not None:
            self.tail.next = new_node
            new_node.prev = self.tail
        else:
            # If there is no list
            self.head = new_node
        self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)
        # # Remove node from the linked list, not from mem
        # self.delete(node)
        # self.length += 1
        # # Point the nodes Next to the current head
        # node.next = self.head
        # # Point the current heads prev to the removed node
        # self.head.prev = node
        # # Reassign the DLL's head to the removed node
        # self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)
        # # Remove node from the linked list, not from mem
        # self.delete(node)
        # self.length += 1
        # # Point the nodes Next to None
        # node.next = None
        # # Point the node tail prev to the current tail
        # node.prev = self.tail
        # # Reassign the DLL's tail to the removed node
        # self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""

    def delete(self, node):

        # If list is empty
        if not self.head:
            print("You got nothing on me")
            return
        self.length -= 1
        # if node is head
        if self.head == self.tail:
            self.head = self.tail = None
        # We have at least two nodes, and the node we want to delete is the head
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        # We have at least two nodes, and the node we want to delete is the tail
        if node == self.tail:
            self.tail = node.prev
            self.tail.next = None
        else:
            node.delete()

    """Returns the highest value currently in the list"""

    def get_max(self):
        # Check to see if there is a self.head
        if not self.head:
            return None
        # Instantiate two values for max value and Current value
        max = self.head.value
        curr = self.head
        # Loop through using truthyness using the curr.next
        while curr:
            # If curr.value is greater then max value
            if curr.value > max:
                # Assign the current value to the max value
                max = curr.value
            # Access the next value in the list using the next property
            curr = curr.next
        # Return next
        return max
