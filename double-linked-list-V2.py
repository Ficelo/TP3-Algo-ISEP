class DoubleLinkedListItem:

    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next

class DoubleLinkedList:

    def __init__(self, items=[]):

        self.head = DoubleLinkedListItem()

        if items:
            for item in items:
                self.append(item)

    def append(self, value):
        
        # Add element at the end of the list

        newItem = DoubleLinkedListItem(value=value)
        
        # If list is empty, make the first element
        if self.head.value == None:
            self.head = newItem
            return
        
        element = self.head

        while element.next != None:
            element = element.next

        newItem.previous = element
        element.next = newItem

    def insert(self, value, position):
        
        # Check that the insert position is in bounds of the list
        if 0 > position or self.getLength() < position:
            return
        
        newItem = DoubleLinkedListItem(value=value)
        element = self.head

        for i in range(0, position):
            element = element.next

        if element == None:
            self.append(value)
            return
        
        if element.previous == None:
            newItem.next = self.head
            self.head.previous = newItem
            self.head = newItem
        else :
            element.previous.next = newItem
            newItem.next = element
            element.previous = newItem

    def insertSorted(self, value):
        
        newItem = DoubleLinkedListItem(value=value)

        if self.head.value is None:
            self.head = newItem
            return

        element = self.head

        if value < self.head.value:
            newItem.next = self.head
            self.head.previous = newItem
            self.head = newItem
            return

        while element.next is not None and element.next.value < value:
            element = element.next

        # Insert newItem in sorted position
        newItem.next = element.next
        newItem.previous = element
        if element.next is not None:
            element.next.previous = newItem
        element.next = newItem

    def get(self, position):
        
        # Check that the insert position is in bounds of the list
        if 0 > position or self.getLength() < position:
            return
        
        element = self.head
        for i in range(0, position):
            element = element.next
        
        return element.value

    def remove(self, position):
        
        # Check that the insert position is in bounds of the list
        if 0 > position or self.getLength() < position:
            return
        
        element = self.head
        
        for i in range(0, position):
            element = element.next
            
        
        if element.previous != None:
            element.previous.next = element.next
            if element.next :
                element.next.previous = element.previous
        else:
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


def sortDoubleLinkedList(list):
    sortedList = DoubleLinkedList()

    element = list.head
    while element is not None:
        sortedList.insertSorted(element.value)
        element = element.next
    
    return sortedList  # Return the sorted list

        

if __name__ == '__main__':
    
    list = DoubleLinkedList([1, 2, 3, 4, 5])
    print(list)
    list.insert(7, 5)
    print(list)
    list.insertSorted(6)
    print(list)
    print(f"get in 3rd position : {list.get(2)}")
    list.remove(2)
    print(list)
    print(f"index of 2: {list.indexOf(2)}")
    print(f"length of list : {list.getLength()}")

    unsorted = DoubleLinkedList([5, 4, 12, 9, 1, 0, 129, 123])
    print(sortDoubleLinkedList(unsorted))