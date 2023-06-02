class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class Deq:
    def __init__(self, value=None):
        self.head = None
        self.endl = None

    def is_empty(self):
        return self.head is None

    def push_back(self, value):
        node_ = Node(value)
        if self.is_empty():
            self.head = node_
            self.endl = node_
        else:
            node_.previous = self.endl
            self.endl.next = node_
            self.endl = node_

    def push_front(self, value):
        node_ = Node(value)
        if self.is_empty():
            self.head = node_
            self.endl = node_
        else:
            node_.next = self.head
            self.head.previous = node_
            self.head = node_

    def pop_front(self):
        if self.is_empty():
            return None
        else:
            elem = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.endl = None
            else:
                self.head.previous = None
            return elem

    def pop_back(self):
        if self.is_empty():
            return None
        else:
            elem = self.endl.value
            self.endl = self.endl.previous
            if self.endl is None:
                self.head = None
            else:
                self.endl.next = None
            return elem

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.value

    def __str__(self):
        result = 'Deq('
        cur = self.head
        count = 0
        while cur:
            if count == 0:
                result += str(cur.value)
                count += 1
            else:
                result += ', ' + str(cur.value)
            cur = cur.next
        result += ')'
        return result

    def __setitem__(self, index, value):
        if 0 <= index < len(self):
            count = 0
            cur = self.head
            while cur:
                if index == count:
                    cur.value = value
                    break
                cur = cur.next
                count += 1
        else:
            raise IndexError("out of range")

    def __copy__(self):
        new_queue = Deq()
        cur = self.head
        while cur:
            new_queue.push_back(cur.value)
            cur = cur.next
        return new_queue
