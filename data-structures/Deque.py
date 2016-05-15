class Node(object):
    """
    Building block of the Deque
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Deque(object):
    """
    Deque implementation built of Node blocks
    """

    def __init__(self):
        self.head = None  # Beginning of the queue
        self.tail = None  # End of Queue
        self.length = 0  # Length stored as a variable for constant time lookup

    def enqueue_first(self, value):
        """
        Adds a value to the beginning of the queue
        :param value: Value to be added to the queue
        :return: nothing
        """
        toinsert = Node(value)
        if self.head == self.tail and self.head is None:
            self.head = toinsert
            self.tail = toinsert
        else:
            toinsert.next = self.head
            self.head = toinsert
        self.length += 1

    def enqueue_last(self, value):
        """
        Adds a value to the end of the queue
        :param value: Value to be added to the queue
        :return: nothing
        """
        toinsert = Node(value)
        if self.head == self.tail and self.tail is None:
            self.head = toinsert
            self.tail = toinsert
        else:
            self.tail.next = toinsert
            self.tail = toinsert
        self.length += 1

    def dequeue_first(self):
        """
        Returns the value at the beginning of the queue
        :return: value at the beginning of the queue, None if queue is empty
        """
        toremove = self.head
        if toremove is None:
            return
        else:
            if self.head.next is None:
                self.tail = self.head = None
            else:
                self.head = self.head.next
            self.length -= 1
        return toremove.value

    def dequeue_last(self):
        """
        Returns the value at the end of the queue
        :return: value at the end of the queue, None if queue is empty
        """
        if self.tail is None:
            return None

        if self.head == self.tail:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            tailprev = self.head
            """
            This can also be implemented using a trailing tail pointer, which always points to the
            Node before the tail pointer
            Edge case : When only one element in present in the Deque
            """
            while tailprev.next is not self.tail:
                tailprev = tailprev.next

            value = self.tail.value
            self.tail = tailprev
            tailprev.next = None
            self.length -= 1
            return value

    def peek_first(self):
        """
        Returns the value in the front of the queue without removing it
        :return: Value in front of the queue, None if queue is empty
        """
        if self.head is None:
            return None
        else:
            return self.head.value

    def peek_last(self):
        """
        Returns the value at the end of the queue without removing it
        :return: Value at the end of the queue, None if queue is empty
        """
        if self.tail is None:
            return None
        else:
            return self.tail.value

    def display(self):
        """
        While loop implementation of displaying the Queue
        :return: nothing
        """
        currentnode = self.head
        while currentnode is not None:
            print currentnode.value,
            if currentnode.next is not None:
                print " -> ",
            currentnode = currentnode.next
        print ""

def main():
    myDeque = Deque()
    myDeque.enqueue_first(10)
    myDeque.enqueue_last(20)
    myDeque.enqueue_first(30)
    myDeque.enqueue_last(70)
    myDeque.display()
    print "Length of Queue : ", myDeque.length
    print "Peeking into the queue (Ssshh !!) : ", myDeque.peek_first()

    myDeque.dequeue_first()
    myDeque.dequeue_last()
    myDeque.dequeue_last()
    myDeque.display()
    print "Length of Queue : ", myDeque.length

if __name__=="__main__": main()