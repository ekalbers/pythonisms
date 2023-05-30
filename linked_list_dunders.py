class LinkedListDunder:
    def __init__(self, head=None):
        self.head = head

    def __getitem__(self, index):
        if index >= len(self) or index < 0:
            raise IndexError('index out of bounds')
        count = 0
        current = self.head
        while count != index:
            current = current.next
            count += 1
        return current.value

    def __setitem__(self, index, value):
        if index >= len(self) or index < 0:
            raise IndexError('index out of bounds')
        count = 0
        current = self.head
        while count != index:
            current = current.next
            count += 1
        current.value = value

    def __eq__(self, other):
        current1 = self.head
        current2 = other.head
        while current1 or current2:
            if current1.value != current2.value:
                return False
            current1 = current1.next
            current2 = current2.next
        return True

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __contains__(self, item):
        current = self.head
        while current:
            if current.value == item:
                return True
            current = current.next
        return False

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next


class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self.next = _next