**Analysis question: briefly explain (3 to 5 sentences) why the linked-list stack pushes at the head instead of the tail, and why the array queue must be circular.**



A linked-list stack pushes at the head because inserting and removing at the head can be done in O(1) time. If the stack pushed at the tail of a singly linked list, it would require searching through the list, making the operation O(n). An array queue must be circular so that empty spaces created after dequeue operations can be reused. The circular design allows the front and rear positions to wrap around to the beginning of the array without shifting the elements.

