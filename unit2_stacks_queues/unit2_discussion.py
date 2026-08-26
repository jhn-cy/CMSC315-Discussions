"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # Hint: A Python list can be used to store stack values.
        self.items = []
        pass

    def push(self, value):
        # this value is the new top in LIFO as it's added to the end
        self.items.append(value)
        pass

    def pop(self):
        # What should happen if the stack is empty? If the stack is empty, an IndexError will be raised if there is no self.is_empty() check. For this, it will return the error message
        if self.is_empty():
            return "Error: Cannot pop from empty stack"
        return self.items.pop()
        pass

    def peek(self):
        # peek return the top item of the stack without removing it - the stack doesn't change
        if self.is_empty():
            return "Error: empty stack - cannot peek"
        return self.items[-1] # the -1 index accesses the last item in a Python list (top of stack) without editing the list
        pass

    def is_empty(self):
        return len(self.items) == 0
        pass


class Queue:
    def __init__(self):
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque() # internal data structure 
        pass

    def enqueue(self, value):
        # adding to the back of the queue = earlier arrivals leave first, which is FIFO
        self.items.append(value)
        pass

    def dequeue(self):
        # Explain or improve empty-queue handling - Error message returned instead of raising an IndexError as there is no front value to remove
        if self.is_empty():
            return "Error: Empty queue - Cannot deque"
        return self.items.popleft()
        pass

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # front returns then next item that would be removed but doesn't remove it
        if self.is_empty():
            return "Error: Cannot view from of empty queue"
        return self.items[0]
        pass

    def is_empty(self):
        return len(self.items) == 0
        pass


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("\n=== STACK DEMO ===")

    stack = Stack()
    print("Adding values 10-70 to the stack.")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)
    stack.push(60)
    stack.push(70)

    print("Top value (peak): ", stack.peek())
    print("The following will remove values via pop() - LIFO")
    print("First pop: ", stack.pop())
    print("Second pop: ", stack.pop())
    print("Third pop: ", stack.pop())
    print("Fourth pop: ", stack.pop())
    print("Fifth pop: ", stack.pop())
    print("Sixth pop: ", stack.pop())
    print("Seventh pop: ", stack.pop())

    print("Try to pop from empty stack: ", stack.pop())
    print("Try to peek at empty stack: ", stack.peek())

    item_stack = Stack()
    item_stack.push("only item")
    print("single-item stack top: ", item_stack.peek())
    print("Removing the only item: ", item_stack.pop())
    print("Verify stack is empty: ", item_stack.is_empty())

    print("\n=== QUEUE DEMO ===")
    queue = Queue()

    print("Adding values 10 - 70 to the queue.")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)
    queue.enqueue(60)
    queue.enqueue(70)

    print("Front value via front(): ", queue.front())
    print("The following demonstrate FIFO via dequeue to remove values:")
    print("First dequeue: ", queue.dequeue())
    print("Second dequeue: ", queue.dequeue())
    print("Third dequeue: ", queue.dequeue())
    print("Fourth dequeue: ", queue.dequeue())
    print("Fifth dequeue: ", queue.dequeue())
    print("Sixth dequeue: ", queue.dequeue())
    print("Seventh dequeue: ", queue.dequeue())

    print("Try to dequeue from empty queue", queue.dequeue())
    print("Try to view front of empty queue", queue.front())

    item_queue = Queue()
    item_queue.enqueue("only item")
    print("single-item queue front: ", item_queue.front())
    print("removing the only item: ", item_queue.dequeue())
    print("verify queue is empty: ", item_queue.is_empty())

if __name__ == "__main__":
    main()
