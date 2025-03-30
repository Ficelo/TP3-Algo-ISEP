class DoubleLinkedListItem:

    def __init__(self, value=None, previous=None, next=None):
        self.value = value
        self.previous = previous
        self.next = next


class DoubleLinkedList:

    def __init__(self, list=[]):
        self.firstElement = DoubleLinkedListItem()
        self.lastElement = DoubleLinkedListItem()

        self.firstElement.next = self.lastElement
        self.lastElement.previous = self.firstElement

        if list != []:
            for item in list:
                self.append(item)
        
    def append(self, value):
        
        newItem = DoubleLinkedListItem(value=value)
        if self.firstElement.value == None:
            self.firstElement.value = value
        elif self.firstElement.value != None and self.lastElement.value == None:
            self.lastElement.value = value
        else:
            self.lastElement.next = newItem
            newItem.previous = self.lastElement
            self.lastElement = newItem

    def insert(self, value, position):
        length = self.get_length()  
        
        if length == 0:
            self.firstElement.value = value
            return

        if position == 0:
            new_element = DoubleLinkedListItem(value, None, self.firstElement)
            self.firstElement.previous = new_element
            self.firstElement = new_element
            return

        if position == length:
            new_element = DoubleLinkedListItem(value, self.lastElement, None)
            self.lastElement.next = new_element
            new_element.previous = self.lastElement
            self.lastElement = new_element
            return

        if 0 < position < length:
            index = 0
            element = self.firstElement
            while index < position - 1:
                index += 1
                element = element.next
            
            new_element = DoubleLinkedListItem(value, element, element.next)
            element.next.previous = new_element
            element.next = new_element

        else:
            print("Impossible d'insérer à cette position.")



    def insert_sorted(self, value):
        index = 0
        element = self.firstElement

        if self.get_length() == 0:
            self.append(value)
            return
        
        if self.firstElement.value != None and self.lastElement.value == None:
            if self.firstElement.value > value:
                self.lastElement.value = self.firstElement.value
                self.firstElement.value = value
            else:
                self.lastElement.value = value

        if value > self.lastElement.value and self.lastElement.value != None:
            el = DoubleLinkedListItem(value, self.lastElement, None)
            self.lastElement.next = el
            self.lastElement = el

        while element.next != None :
            if element.value > value:
                self.insert(value, index)
                return
            index += 1
            element = element.next



    def get(self, index):
        element = self.firstElement

        if index < 0 or index > self.get_length() - 1:
            return None

        for n in range (0, index):
            element = element.next
        return element.value


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


    def indexOf(self, value):
        
        element = self.firstElement
        index = 0

        while element != None:
            if element.value == value:
                return index
            index += 1
            element = element.next

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
    


if __name__ == '__main__':
    test = DoubleLinkedList([1, 2, 3, 4, 5])
    print(test)
    test.insert(2.5, 2)
    print(test)
    print(test.get_length())
    test.insert(0.1, 0)
    print(test)
    test.insert_sorted(0.001)
    print(test)

    test2 = DoubleLinkedList()
    test2.insert_sorted(1)
    test2.insert_sorted(-1)
    test2.insert_sorted(4)
    print(test2)
    print(test2.get(0))
    print(test2.indexOf(5))


    element = test.firstElement
    while element is not None:
        print(f"Value: {element.value}, "
            f"Next value: {element.next.value if element.next else None}, "
            f"Previous value: {element.previous.value if element.previous else None}")
        element = element.next