class Node:
    def __init__(self, val):
        self.val = val          # Store int value
        self.next = None        # Pointer refers to the next node in the list

class MyLinkedList:

    def __init__(self):
        self.head = None                # Points to the first node (None if empty)
        self.size = 0                   # Tracks number of nodes in the list

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1                   # Out of bounds check
        
        curr = self.head

        for _ in range(index): 
            curr = curr.next          # Walk to target index

        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size: 
            return
        if index < 0: 
            index = 0

        new_node = Node(val)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            curr = self.head
            for _ in range(index - 1): 
                curr = curr.next                        # Stops before the index

            new_node.next = curr.next    
            curr.next = new_node
            
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size: 
            return
        if index == 0:
            self.head = self.head.next
        else:
            curr = self.head
            for _ in range(index -1): 
                curr = curr.next      # Stop right before index
            curr.next = curr.next.next                      # Bypass target node
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)