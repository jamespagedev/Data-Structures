from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList
import random
import time

def get_list_ints():
    return [i for i in range(1, 100000)]

def create_doubly_linked_list_numbers():
    dll = DoublyLinkedList(ListNode(1))
    for i in range(2, 100000):
        dll.add_to_tail(i)
    return dll

def get_middle_node(dll):
    current = dll.head
    for i in range(50000):
        current = current.next
    return current

rnd_list = get_list_ints()

doubly_link_list = create_doubly_linked_list_numbers()

start = time.time()
sObject = slice(99998)
print(rnd_list[sObject])
end = time.time()
print(end - start)

start = time.time()
node = get_middle_node(doubly_link_list)
print(doubly_link_list.delete(node))
end = time.time()
print(end - start)