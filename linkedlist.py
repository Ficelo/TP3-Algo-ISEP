
class LinkedListItem:

   def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
    

class LinkedList:

    def __init__(self, items=[]):
        self.firstElement = LinkedListItem()
        self.lastElement = LinkedListItem()

        self.firstElement.next = self.lastElement
        self.lastElement.next = None

        if items != []:
            for item in items:
                self.append(item)

    def append(self, item):
        newItem = LinkedListItem(value=item)
        if self.firstElement.value == None:
            self.firstElement.value = item
        elif self.firstElement.value != None and self.lastElement.value == None:
            self.lastElement.value = item
        else:
            self.lastElement.next = newItem
            self.lastElement = newItem

    def insert(self, item, position):

        if self.get_length() == 0:
            self.firstElement.value = item
            

        if position == 0:

            if self.lastElement.value == None:
                self.lastElement.value = self.firstElement.value
                self.firstElement.value = item
                return

            el = LinkedListItem(item, self.firstElement)
            self.firstElement = el
            return

        if position == self.get_length() - 1:
            el = LinkedListItem(item, None)
            self.lastElement.next = el
            self.lastElement = el
            return


        if position < self.get_length() and position >= 0:

            index = 0
            element = self.firstElement

            while(index < position - 1):
                index += 1
                element = element.next
            
            el = LinkedListItem(item, element.next)
            element.next = el
            

        else:
            print("Impossible d'insérer à cette position.")

    def insert_sorted(self, item):
        element = self.firstElement

        if(self.firstElement.value == None):
            self.firstElement.value = item
            return
        if(self.lastElement.value == None):
            self.lastElement.value = item
            return

        if(self.lastElement.value <= item):
            el = LinkedListItem(item, None)
            self.lastElement.next = el
            self.lastElement = el
            return

        if(self.firstElement.value >= item):
            el = LinkedListItem(item, self.firstElement)
            self.firstElement = el
            return

        while element.next != None:
            if element.next.value >= item:
                el = LinkedListItem(item, element.next)
                element.next = el
                return
            element = element.next
            
    def get(self, position):
        
        if(position >= self.get_length()):
            return None
        
        index = 0
        element = self.firstElement

        while index < position:
            element = element.next
            index += 1
        
        return element

    def remove(self, position):
        index = 0
        element = self.firstElement
        while index < position - 1:
            index += 1
            element = element.next
        element.next = element.next.next
        
    def get_length(self):

        if self.firstElement.value == None and self.lastElement.value == None:
            return 0
        if self.firstElement.value != None and self.lastElement.value == None:
            return 1

        length = 1
        element = self.firstElement
        while(element.next != None):
            length += 1
            element = element.next
        return length

    def indexOf(self, item):
        
        index = 0
        element = self.firstElement

        while element != None:
            if element.value == item:
                return index
            index += 1
            element = element.next

        return None

    def __repr__(self):
        
        if self.firstElement.value == None and self.lastElement.value == None:
            return "[]"
        if self.firstElement.value != None and self.lastElement.value == None:
            return f"[{self.firstElement.value}]"


        element = self.firstElement
        string = "["

        while(element.next != None):
                string += f"{element.value}, "
                element = element.next
        
        string += f"{self.lastElement.value}]"
        
        return string


def sortLinkedList(list):

    sortedList = LinkedList()

    element = list.firstElement
    while element != None:
        sortedList.insert_sorted(element.value)
        element = element.next

    return sortedList

class Queue(LinkedList):

    def pop(self):
        self.firstElement = self.firstElement.next

    def push(self, item):
        self.append(item)

    def empty(self):
        self.firstElement.value = None
        self.lastElement.value = None
        self.firstElement.next = self.lastElement

    def isEmpty(self):
        return self.firstElement.value == None and self.lastElement.value == None and self.firstElement.next == self.lastElement

class Stack(LinkedList):
    
    def pop(self):
        self.firstElement = self.firstElement.next  

    def push(self, item):
        if self.firstElement.value == None:
            self.firstElement = LinkedListItem(item, self.lastElement)
        else:
            self.insert(item, 0)

    def empty(self):
        self.firstElement.value = None
        self.lastElement.value = None
        self.firstElement.next = self.lastElement

    def isEmpty(self):
        return self.firstElement.value == None and self.lastElement.value == None and self.firstElement.next == self.lastElement

if __name__ == '__main__':

    
    test = LinkedList([1])
    test.insert(0, 0)
    print(test)

    # unsorted = LinkedList([6, 7, 5, 3, 9, 1, 9, 0, 2, 17, 89, 32])
    # print(unsorted)
    # print(sortLinkedList(unsorted))

    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    print(f"Queue : {queue}")
    print(f"Queue is empty ? : {queue.isEmpty()}")

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    print(f"Stack : {stack}")
    print(f"Stack is empty ? : {stack.isEmpty()}")

    queue.pop()
    print(f"Queue : {queue}")

    stack.pop()
    print(f"Stack : {stack}")

    queue.empty()
    print(f"Queue : {queue}")

    stack.empty()
    print(f"Stack : {stack}")

    
    print(f"Queue is empty ? : {queue.isEmpty()}")
    print(f"Stack is empty ? : {stack.isEmpty()}")
    
