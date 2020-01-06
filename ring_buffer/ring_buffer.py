from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.storage.length == self.capacity:
            if self.current is None:
                self.storage.remove_from_head()
                self.storage.add_to_head(item)
                self.current = self.storage.head.next
                return
            self.current.value = item    
            self.current = self.current.next    
            return
        self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        if self.storage.head is None:
            return list_buffer_contents
        current_node = self.storage.head
        ln = int(0)
        while ln <= self.storage.length:
            if current_node is None:
                return list_buffer_contents
            if current_node.value is not None:
                list_buffer_contents.append(current_node.value)
            current_node = current_node.next
            ln +=1
        print('buff',list_buffer_contents)
        return list_buffer_contents
# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
