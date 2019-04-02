Answer the following questions for each of the data structures you implemented as part of this project.

Reference - https://wiki.python.org/moin/TimeComplexity

## Queue

1. What is the runtime complexity of `enqueue`?
    `Queue.insert()`, time complexity will be O(n)

2. What is the runtime complexity of `dequeue`?
    `Queue.pop()`, time complexity will be O(1)

3. What is the runtime complexity of `len`?
    Python automatically stores the len of a data structure everytime it gets initialized.
    Therefor, since it's already in memory, it just needs to point to the address to obtain the value.
    This means the time complexity will be O(1)

## Binary Search Tree

1. What is the runtime complexity of `insert`?

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`?

## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
O(1)

3. What is the runtime complexity of `ListNode.delete`?
O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
Best Case = O(1)
Average Case = O(n)
Worst Case = O(n)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
Best Case = O(1)
Average Case = O(n)
Worst Case = O(n)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?