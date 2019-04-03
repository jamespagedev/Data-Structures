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
* Worst Case -> O(h) - where h is the height of the tree.
* Best Case -> O(log n) - since the tree contains n nodes that have a minimum of O(log n) levels, it takes at least O(log n) comparisons to find a particular node.
* Average Case -> O(n) - a binary serch tree can degenerate to a linked list, reducing the search time to O(n).

2. What is the runtime complexity of `contains`?
Nearly the same logic as the insert, but instead of assigning the next node a None, it checks the current node value.
Because the traversal is the same, the iterations until found can be the same as insert.
* Worst Case -> O(h) - where h is the height of the tree.
* Best Case -> O(log n) - since the tree contains n nodes that have a minimum of O(log n) levels, it takes at least O(log n) comparisons to find a particular node.
* Average Case -> O(n) - a binary serch tree can degenerate to a linked list, reducing the search time to O(n).

3. What is the runtime complexity of `get_max`?
Much like the contains traversal, it must also check every increasing value until the final increasing value is found.
However, because this search will only go in one direction (to the right), it removes the danger of having the tree degernate into a link list.
* Worst Case -> O(h) - where h is the height of the tree.
* Best Case -> O(log n) - since the tree contains n nodes that have a minimum of O(log n) levels, it takes at least O(log n) comparisons to find a particular node.
* Average Case -> O(log n)

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
    given a number of 100,000 iterations the slice of the (full array - 1) is "0.08600497245788574", and...
        delete(head_node) = "0.0"
        delete(tail_node) = "0.0"
        delete(middle_node) = "0.003000020980834961"
    the comparison is 28x faster