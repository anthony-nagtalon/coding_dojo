class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        new_node.next = self.head
        self.head = new_node
        return self

    def print_values(self):
        cur_node = self.head
        while cur_node != None:
            print(cur_node.value)
            cur_node = cur_node.next
        return self

    def add_to_back(self, val):
        if self.head == None:
            self.add_to_front(val)

        else:
            new_node = SLNode(val)
            cur_node = self.head
            while cur_node.next != None:
                cur_node = cur_node.next
            cur_node.next = new_node
            return self

    def remove_from_front(self):
        if self.head == None:
            print("Invalid: List is already empty!")
        else:
            self.head = self.head.next
        return self

    def remove_from_back(self):
        # Edge case: size == 0
        if self.head == None:
            print("Invalid: List is already empty!")
        # Edge case: size == 1
        elif self.head.next == None:
            self.head == None
        else:
            cur_node = self.head
            while cur_node.next.next != None:
                cur_node = cur_node.next
            cur_node.next = None
        return self

    def remove_val(self, val):
        # Edge case: size == 0
        if self.head == None:
            print("Invalid: List is already empty!")
        else:
            cur_node = self.head
            prev_node = None
            # Edge case: Node to remove is list head
            if cur_node.value == val:
                self.remove_from_front()
            else:
                removed = False
                while cur_node != None:
                    prev_node = cur_node
                    cur_node = cur_node.next
                    if cur_node != None and cur_node.value == val:
                        prev_node.next == cur_node.next
                        remove_success = True
                if not remove_success:
                    print('Invalid: "{}" is not in list.'.format(val))

        return self


my_list = SList()
my_list.add_to_front(2).add_to_front(1).add_to_back(3).add_to_back(4)
my_list.remove_val(4).print_values()
