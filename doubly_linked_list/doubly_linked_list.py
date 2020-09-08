"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length


    """
    Wraps the given value in a ListNode and inserts it
    as the new head of the list. Don't forget to handle
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        #                         prev   next
        new_node = ListNode(value, None, None)
        # if list is empty add new node to head and tail
        if self.head is None and self.tail is None:
        # set the head and tail to equal the new node
           self.head = new_node
           self.tail = new_node
        else:
        # the list already has elements in it
        # make new nodes next value print to current head
            new_node.next = self.head 
            self.head = new_node
   


    # """
    # Removes the List's current head node, making the
    # current head's next node the new head of the List.
    # Returns the value of the removed Node.
    # """

    # def remove_from_head(self):
    #     pass
  

    # """
    # Wraps the given value in a ListNode and inserts it 
    # as the new tail of the list. Don't forget to handle 
    # the old tail node's next pointer accordingly.
    # """

    def add_to_tail(self, value):
           #                       prev   next
        new_node = ListNode(value, None, None)
        # if list is empty add new node to head and tail
        self.length += 1
        if self.head is None and self.tail is None:
        # set the head and tail to equal the new node
           self.head = new_node
           self.tail = new_node
        else:
        # the list already has elements in it
        # make new nodes next value print to current head
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node

    # """
    # Removes the List's current tail node, making the 
    # current tail's previous node the new tail of the List.
    # Returns the value of the removed Node.
    # """

    # def remove_from_tail(self):
    #     pass

    # """
    # Removes the input node from its current spot in the 
    # List and inserts it as the new head node of the List.
    # """

    # def move_to_front(self, node):
    #     pass

    # """
    # Removes the input node from its current spot in the 
    # List and inserts it as the new tail node of the List.
    # """

    # def move_to_end(self, node):
    #     pass

    # """
    # Deletes the input node from the List, preserving the 
    # order of the other elements of the List.
    # """

    def delete(self, node):
        # the list is empty do nothing
        if self.head is None and self.tail is None:
            return
        # the list is only one node
        if self.head == self.tail and node == self.head:
            self.head = None
            self.tail = None
        # the node is the head node (make sure to handle head pointer properly)
        if self.head == node:
            self.head = node.next


        # the node is the tail ( make sure tail is handled correctly)
        # the node is just some node in the list
        

    # """
    # Finds and returns the maximum value of all the nodes 
    # in the List.
    # """

    # def get_max(self):
    #     pass

