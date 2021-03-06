class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    # def get_length():
    #     return self.length
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        output = ''
        cur_node = self.head
        while cur_node is not None:
            output += f"{cur_node.get_value()} -> "
            cur_node = cur_node.get_next()
        return output

    def add_to_head(self, value):
        new_node = Node(value, self.head)
        self.head = new_node
        if self.length == 0:    
            self.tail = new_node
        self.length += 1

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
        else:
            self.tail.set_next(new_node)
        self.tail = new_node
        self.length += 1

    def remove_head(self):
        if self.head is None:
            return None
        # list with one nodes
        elif self.head == self.tail: # this works because we checked to see if the head was None first - if head was None, tail would be None and things would break
            head_value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        # list with 2+ nodes
        else:
            head_value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return head_value

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.head == self.tail:
            # tail_value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return self.tail.get_value()
        else:
            tail_value = self.tail
            cur_node = self.head
            while cur_node.get_next() is not self.tail:
                cur_node = cur_node.get_next()
            cur_node.set_next(None)
            self.length -= 1
            return tail_value

    def contains(self, value):
        if self.head is None and self.tail is None:
            return False
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next()
        return False


my_ll = LinkedList()
my_ll.add_to_head(0)
my_ll.add_to_tail(1)
my_ll.add_to_tail(6)
my_ll.remove_tail()
my_ll.remove_head()
print(my_ll)
print(my_ll.length)
# print(my_ll.tail)