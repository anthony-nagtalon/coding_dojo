class Node:
    def __init__(self, val):
        self.value = val
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            # Adjusts end node if list is circular
            if not new_node.prev == None:
                new_node.prev.next = new_node
        return self

    def add_to_back(self, val):
        new_node = Node(val)
        if self.head == None:
            self.head = new_node
        else:
            cur_node = self.head
            while not cur_node.next == None and not cur_node.next == self.head:
                cur_node = cur_node.next
            new_node.prev = cur_node
            new_node.next = cur_node.next
            cur_node.next = new_node
            # Adjusts head.prev if list is circular
            if not new_node.next == None:
                new_node.next.prev = new_node
        return self

    def insert_at(self, val, n):
        if n == 0 or self.head == None:
            self.add_to_front(val)
        else:
            new_node = Node(val)
            cur_node = self.head
            for i in range(n):
                if cur_node.next == None or cur_node.next == self.head:
                    print("Invalid: n = {} is out of list size.".format(n))
                    return self
                cur_node = cur_node.next
            prev_node = cur_node.prev

            # Insert node, adjust connections:
            new_node.next = cur_node
            new_node.prev = prev_node
            prev_node.next = new_node
            cur_node.prev = new_node

        return self

    # i = The number instance of the given to insert after
    # IE. Inserting after the second instance of 2 in the list
    def insert_after(self, val, given, i = 0):
        if self.head == None:
            print("Invalid: List is empty.")
        else:    
            cur_node = self.head
            new_node = Node(val)
            while True:
                # Compare val
                if cur_node.value == given:
                    if i > 0:
                        i -= 1
                    else:
                        new_node.next = cur_node.next
                        new_node.prev = cur_node
                        cur_node.next = new_node
                        if new_node.next != None:
                            new_node.next.prev = new_node
                        return self
                cur_node = cur_node.next
                if cur_node == None or cur_node == self.head:
                    break
            print("Invalid: {} is not in list or not enough duplicates exist in list.".format(given))
        return self

    def print_values(self):
        cur_node = self.head
        while True:
            print(cur_node.value)
            cur_node = cur_node.next
            if cur_node == None or cur_node == self.head:
                break

    # Test function - Links list circularly to test cases
    def link_circular(self):
        cur_node = self.head
        while not cur_node.next == None:
            cur_node = cur_node.next
        cur_node.next = self.head
        self.head.prev = cur_node
        return self


list = DoublyLinkedList()
list.add_to_front(3).add_to_front(2).add_to_front(1)
list.add_to_front(0).add_to_back(4).add_to_back(5)
list.insert_at(4.5, 5)
list.insert_after(4.6, 4.5).add_to_back(5).insert_after(6, 5, 1).insert_after(1, 5, 2).print_values()
