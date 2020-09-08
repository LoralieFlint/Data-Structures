""" creates Node class """


class Node:
    """ initializes function """

    def __init__(self, value=None, next_node=None):
        """ the value at this linked list node """
        self.value = value
        """ reference to the next node in the list """
        self.next_node = next_node

    def get_value(self):
        """ return self.length """
        return self.value

    def get_next(self):
        """ moves pointer to next node """
        return self.next_node

    def set_next(self, new_next):
        """ set this node's next_node reference to the passed in node """
        self.next_node = new_next


""" creates LinkedList class """


class LinkedList:
    def __init__(self):
        """ initializes head tail and length """
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """ outputs a formatted string of current node value more readable in the console """
        output = ''
        cur_node = self.head
        while cur_node is not None:
            output += f"{cur_node.get_value()} -> "
            cur_node = cur_node.get_next()
        return output

    def get_length(self):
        return self.length

    def add_to_head(self, value):
        # if self.head is None:
        #     new_node = Node(value, None)
        #     self.head = new_node
        #     self.tail = new_node
        #     self.length += 1
        # else:
        #     new_node = Node(value, self.head)
        #     self.head = new_node
        #     self.length += 1
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
        elif self.head == self.tail:  # this works because we checked to see if the head was None first - if head was None, tail would be None and things would break
            head_value = self.head.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return head_value
        else:
            head_value = self.head.get_value()
            self.head = self.head.get_next()
            self.length -= 1
            return head_value


    def remove_tail(self):
        if self.head is None:
            return None
        elif self.tail == self.head:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return value
        else:
            cur_node = self.head
            while cur_node.get_next() is not None:
                cur_node = cur_node.get_next()
            value = self.tail.get_value()
            cur_node.set_next(None)
            self.tail = cur_node
            self.length -= 1
            return value

    def contains(self, value):
        if self.head is None and self.tail is None:
            return False
        cur_node = self.head
        while cur_node is not None:
            if cur_node.get_value() == value:
                return True
            cur_node = cur_node.get_next()
        return False


