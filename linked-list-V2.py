class LinkedListItem:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:

    def __init__(self, items=[]):
        
        self.head = LinkedListItem()
        
        if items:
            for item in items:
                self.append(item)
    
    def append(self, value):

        # Add element at the end of the list

        newItem = LinkedListItem(value=value)

        # If list is empty, make the first element
        if self.head.value == None:
            self.head = newItem
            return
        
        element = self.head
        previous = None

        while element != None:
            previous = element
            element = element.next

        previous.next = newItem

    def insert(self, value, position):
        
        # Check that the insert position is in bounds of the list
        if 0 > position or self.getLength() - 1 < position:
            return

        newItem = LinkedListItem(value=value)

        element = self.head
        previous = None
        for i in range(0, position):
            previous = element
            element = element.next
        
        if previous == None:
            newItem.next = self.head
            self.head = newItem
        else:
            previous.next = newItem
            newItem.next = element
            
    def insertSorted(self, value):
        
        if self.head.value == None:
            self.head.value = value
            return

        newItem = LinkedListItem(value=value)

        element = self.head
        previous = None

        while element != None and element.value < value:
            previous = element
            element = element.next
        
        
        previous.next = newItem
        newItem.next = element

    def get(self, position):
        
        # Check that the insert position is in bounds of the list
        if 0 > position or self.getLength() - 1 < position:
            return

        element = self.head
        for i in range(0, position):
            element = element.next
        
        return element.value

    def remove(self, position):
        
        # Check that the insert position is in bounds of the list
        if 0 > position or self.getLength() - 1 < position:
            return
        
        element = self.head
        previous = None

        for i in range(0, position):
            previous = element
            element = element.next

        if previous:
            previous.next = element.next
        else :
            if self.head.next:
                self.head = self.head.next
            else:
                self.head.value = None

    def indexOf(self, value):
        
        element = self.head
        index = 0

        while element:
            if element.value == value:
                return index
            index += 1
            element = element.next

    def getLength(self):

        if self.head.value == None:
            return 0
        
        size = 0

        element = self.head
        while element != None:
            size += 1
            element = element.next
        
        return size

    def __repr__(self):

        elements = []
        element = self.head
        while element is not None and element.value is not None:
            elements.append(str(element.value))
            element = element.next
        return "[" + ", ".join(elements) + "]"


def sortLinkedList(list):

    sortedList = LinkedList()

    element = list.head
    while(element):
        sortedList.insertSorted(element.value)
        element = element.next
    return sortedList


class Stack(LinkedList):
    
    def __init__(self, list=[]):
        super().__init__(list)

    def pop(self):

        if self.head is None or self.head.value is None:
            return

        if self.head.next:
            self.head = self.head.next
        else:
            self.head.value = None

    def push(self, value):
        newItem = LinkedListItem(value=value)
        newItem.next = self.head
        self.head = newItem

    def empty(self):
        self.head.value = None
        self.head.next = None

    def isEmpty(self):
        return self.head.next == None

class Queue(LinkedList):
    
    def pop(self):
        if self.head is None or self.head.value is None:
            return

        if self.head.next:
            self.head = self.head.next
        else:
            self.head.value = None

    def push(self, value):
        
        newItem = LinkedListItem(value)

        if self.head is None or self.head.value is None:
            self.head = newItem
            return
        
        element = self.head

        while element.next != None:
            element = element.next

        element.next = newItem

    def empty(self):
        self.head.value = None
        self.head.next = None

    def isEmpty(self):
        return self.head.next == None


if __name__ == '__main__':
    # list = LinkedList([1, 2, 3, 4, 5])
    # print(list)
    # print(f"size : {list.getLength()}")
    # list.insert(3.5, 3)
    # print(list)
    # list.insertSorted(4.5)
    # print(list)
    # print(list.get(2))
    # list.remove(0)
    # print(list)
    # print(list.indexOf(2))

    # unsortedList = LinkedList([3, 5, 9, 10, 28, 57, 28, 9, 29, 88, 21, 4, 213])
    # print(sortLinkedList(unsortedList))

    # stack = Stack()

    # stack.push(1)
    # stack.push(2)
    # stack.push(3)

    # print(stack)

    # stack.pop()

    # print(f"is empty : {stack.isEmpty()}")

    # stack.empty()

    # print(f"is empty : {stack.isEmpty()}")
    

    # print(stack)

    queue = Queue()

    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(queue)

    queue.pop()

    print(f"is empty : {queue.isEmpty()}")

    queue.empty()

    print(f"is empty : {queue.isEmpty()}")
    
    print(queue)

