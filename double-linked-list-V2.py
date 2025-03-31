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
        pass

    def insert(self, value, position):
        pass

    def insertSorted(self, value):
        pass

    def get(self, position):
        pass

    def remove(self, position):
        pass

    def indexOf(self, value):
        pass

    def getLength(self):
        pass

    def __repr__(self):
        pass

    if __name__ == '__main__':
        pass