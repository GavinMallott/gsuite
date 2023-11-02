# Gavin's Data Structures
# Gavin Mallott
# 10/31/23

# --- Imports --- #


# --- Stack -- #
class Stack:
    "LIFO"

    def __init__(self, items=None):
        if items is None:
            items = list()
            self.length = 0
        else:
            self.length = len(items)

        self.stack = items

    def __str__(self):
        if self.length > 0:
            return str(self.stack)
        else:
            return ""

    def __repr__(self):
        return self.stack

    def push(self, item):
        self.stack.append(item)
        self.length += 1
        return self.stack

    def pop(self):
        if self.length > 0:
            self.length -= 1
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if self.length > 0:
            return self.stack[-1]
        else:
            return None


# --- Queue -- #
class Queue:
    "FIFO"

    def __init__(self, items=None):
        if items is None:
            items = list()
            self.length = 0
        else:
            self.length = len(items)

        self.queue = items

    def __str__(self):
        if self.length > 0:
            return str(self.queue)
        else:
            return ""

    def __repr__(self):
        return self.queue

    def push(self, item):
        self.queue.append(item)
        self.length += 1
        return self.queue

    def pop(self):
        if self.length > 0:
            self.length -= 1
            new_queue = self.queue[1:]
            popped_item = self.queue[0]

            self.queue = new_queue
            return popped_item
        else:
            return None

    def peek(self):
        if self.length > 0:
            return self.queue[0]
        else:
            return None


# --- Heap -- #
class Heap:
    def __init__(self):
        pass


# --- MaxHeap -- #
class MaxHeap:
    def __init__(self):
        pass


# --- LinkedList -- #
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return self.value


class DELinkedList:
    def __init__(self):
        self.root = None
        self.length = 0

    def __str__(self):
        return f"{self!r}"

    def __repr__(self):
        if self.length > 0:
            current = self.root
            retval = [current.value]
            while current.next:
                current = current.next
                retval.append(current.value)
            return retval
        else:
            return None

    def push(self, item, right=False):
        if right:
            return self.push_right(item)
        else:
            return self.push_left(item)

    def push_left(self, item):
        new_node = Node(item)
        if self.length > 0:
            new_node.next = self.root

        self.root = new_node
        self.length += 1
        return self.root

    def push_right(self, item):
        new_node = Node(item)
        if self.length > 0:
            current = self.root
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.root = new_node

        self.length += 1
        return self.root

    def pop(self, right=False):
        if right:
            return self.pop_right()
        else:
            return self.pop_left()

    def pop_left(self):
        if self.length > 0:
            retval = self.root.value
            self.root = self.root.next
            self.length -= 1
            return retval
        else:
            return None

    def pop_right(self):
        if self.lenth > 0:
            current = self.root
            previous = None
            while current.next:
                previous = current
                current = current.next
            previous.next = None
            self.length -= 1
            return current.value
        else:
            return None


# --- CircularLinkedList -- #
class CircularLinkedList(LinkedList):
    def __init__(self):
        pass


# --- Tree -- #
class Tree:
    def __init__(self):
        pass


# --- BinaryTree -- #
class BinaryTree:
    def __init__(self):
        pass


# --- Graph -- #
class Graph:
    def __init__(self):
        pass


# --- HashTable -- #
class HashTable:
    def __init__(self):
        pass


if __name__ == "__main__":
    pass
