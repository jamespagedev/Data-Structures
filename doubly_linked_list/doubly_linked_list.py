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

    def add_to_head(self, value):
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.head.prev = new_node
            self.head.prev.next = self.head
            self.head = new_node
            self.length += 1

    def remove_from_head(self):
        old_value = self.head.value
        if self.head and self.__len__() == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.head:
            self.head.next.prev = None
            self.head = self.head.next
            self.length -= 1
        return old_value

    def add_to_tail(self, value):
        new_node = ListNode(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail.next.prev = self.tail
            self.tail = new_node
            self.length += 1

    def remove_from_tail(self):
        old_value = self.tail.value
        if self.tail and self.__len__() == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif self.tail:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.length -= 1
        return old_value

    def move_to_front(self, node):
        node_value = node.value
        if self.head is node:
            self.remove_from_head()
        elif self.tail is node:
            self.remove_from_tail()
        else:
            self.delete(node)
        self.add_to_head(node_value)

    def move_to_end(self, node):
        node_value = node.value
        self.delete(node)
        self.add_to_tail(node_value)

    def delete(self, node):
        if self.head is node:
            self.remove_from_head()
        elif self.tail is node:
            self.remove_from_tail
        else:
            self.length -= 1
            node.delete()

    def get_max(self):
        if self.head is self.tail:
            return self.head.value

        value = self.head.value
        node_in_check = self.head
        while node_in_check.next is not None:
            node_in_check = node_in_check.next
            if node_in_check.value > value:
                value = node_in_check.value
        return value
