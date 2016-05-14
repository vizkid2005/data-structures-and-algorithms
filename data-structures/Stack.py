class Node(object):
    """
    The building block of a Stack
    Can be used as a building block of LinkedList too
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack(object):
    """
    Implementation of stack using Node instances
    """
    def __init__(self):
        self.top = None

    def push(self, value):
        """
        Adding element to top of stack
        :param value: Value to add at the top of stack
        :return: nothing
        """
        toPush = Node(value)
        toPush.next = self.top
        self.top = toPush

    def pop(self):
        """
        Remove a Node object from top of the stack
        :return: The element value at top of stack
        """
        if self.top is None:
            return
        else:
            todelete = self.top
            self.top = todelete.next
            return todelete.value

    def display(self):
        """
        Wrapper for the display function
        :return: void
        """
        self.recursive_display(self.top)

    def recursive_display(self, node):
        """
        Recursive implementation of displaying the stack
        :param node: the top node
        :return: void
        """
        if node is None:
            print ""
            return
        else:
            print node.value
            self.recursive_display(node.next)


def main():
    mystack = Stack()
    mystack.push(10)
    mystack.push(20)
    mystack.push(30)
    mystack.push(40)
    mystack.display()

    mystack.pop()
    mystack.pop()
    mystack.pop()
    mystack.display() # Displays the last element in the stack

    mystack.pop()
    mystack.pop()
    mystack.display()  # Displays empty stack

if __name__ == "__main__": main()