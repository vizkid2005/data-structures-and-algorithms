class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    # Positions in this list begin from 1
    def __init__(self, head=None):
        self.head=None
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else :
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            
    def get_position(self, position):
        current = self.head
        while current:
            if position == 1:
                return current.value
            position -= 1
            current = current.next
        return None
    
    def display(self):
        current = self.head
        while current:
            print current.value, " ", 
            current = current.next
        print ""

    def delete(self, value):
        current = self.head
        if current.value == value:  # Handling Edge case for 1st position
            self.head = current.next
            return
        while current:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    def insert(self, value, position):
        toinsert = Node(value)
        if position == 1:  # Handling edge case for 1st position
            toinsert.next = self.head
            self.head = toinsert
            return
        
        currentposition = 1
        current = self.head
        while current:
            if currentposition + 1 == position:
                toinsert.next = current.next
                current.next= toinsert
            currentposition += 1
            current = current.next


def main():

    myList = LinkedList()
    myList.append(10)
    myList.append(20)
    myList.append(30)
    myList.append(40)
    myList.display()
    myList.insert(60,3)
    myList.display()
    myList.insert(70,100)  # Will not insert any element for invalid position, can throw error for handling
    myList.display()
    myList.insert(70, 5)  # Checking edge case for Last element
    myList.display()
    myList.insert(100, 1)  # Checking edge case for First element
    myList.display()
    myList.delete(60)
    myList.display()
    myList.delete(100)  # Edge case first element
    myList.display()
    myList.delete(40)  # Edge case last element
    myList.display()

if __name__ == "__main__" : main()