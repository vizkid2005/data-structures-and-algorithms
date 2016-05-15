class Node(object):
    """
    Building block of Queue
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    """
    Queue implementation built of Node blocks
    """
    def __init__(self):
        self.head = None  # Beginning of the queue
        self.tail = None  # End of Queue
        self.length = 0   # Length stored as a variable for constant time lookup

    def enqueue(self, value):
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

    def dequeue(self):
        """
        Returns the value at the beginning of the queue
        :return: value at the beginning of the queue
        """
        if self.head is None:
            self.tail = self.head # When queue is empty, head and tail should point to None
            return
        else:
            toremove = self.head
            self.head = self.head.next
            self.length -= 1
            return toremove.value

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

    myqueue = Queue()
    myqueue.display()

    myqueue.enqueue(10)
    myqueue.enqueue(20)
    myqueue.enqueue(30)

    myqueue.display()
    print "Length of Queue : ", myqueue.length

    myqueue.dequeue()
    myqueue.dequeue()

    myqueue.display()
    print "Length of Queue : ", myqueue.length

    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    myqueue.dequeue()
    print "Length of Queue : ", myqueue.length

    myqueue.enqueue(10)
    myqueue.enqueue(20)
    myqueue.enqueue(30)

    myqueue.display()
    print "Length of Queue : ", myqueue.length

if __name__ == "__main__": main()