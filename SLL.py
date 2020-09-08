class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


def add_to_head(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
        self.head = new_node
        self.tail = new_node
    else:
        new_node.next_node = self.head
        self.head = new_node


def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
        self.head = new_node
        self.tail = new_node
    else:
        self.tail.next_node = new_node
        self.tail = new_node


def remove_head(self):
    if not self.head:
        return None
    if self.head.next_node is None:
        head_value = self.head.value
        self.head = self.head.next_node
    return head_value


def contains(self, value):
    if self.head is None:
        return False
    current_node = self.head
    while current_node is not None:
        if current_node.value == value:
            return True
    current_node = current_node.next_node
    return False

# linked_list = LinkedList()
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# # print(linked_list.head.value)
# # print(linked_list.tail.value)
# # print(f'does our LLcontain 0? {linked_list.contains(0)}')
# # print(f'does our LLcontain 1? {linked_list.contains(1)}')
# # print(f'does our LLcontain 3? {linked_list.contains(3)}')
# # linked_list.add_to_head(2)
# # print(f'does our LLcontain 2 after adding it to the head? {linked_list.contains(2)}')
# # linked_list.remove_head(2)
# # print(f'does our LLcontain 2 after removing the head? {linked_list.contains(2)}')
# linked_list.add_to_tail(2)
# linked_list.add_to_tail(3)
# print(linked_list)
