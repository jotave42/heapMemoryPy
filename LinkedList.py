from HeapNode import HeapNode
class LinkedList:
    head = None
    size = 0
    def __init__(self, size):
        self.size =size
        self.head = HeapNode(None,None,0,size)

    def getPrintableFreeBlocksList(self):
        freeNode= self.head
        nodesStringArray = []
        while freeNode is not None:
            nodesStringArray.append('[Position Free = %(position)s | Free Blocks = %(freeBlocks)d]' % {"position": freeNode.getPosition(), "freeBlocks": freeNode.getFreeBlocks()})
            freeNode = freeNode.getNextNode()
        return "->".join(nodesStringArray)
    
    def __iter__(self):
        linkedListnode = self.head
        while linkedListnode is not None:
            yield linkedListnode
            linkedListnode = linkedListnode.getNextNode()

    def __next__(self):
         linkedListnode = self.head
         return linkedListnode.getNextNode()
    def getHead(self):
        return self.head
    def setHead(self,head):
         self.head = head
    def removeFromFreeSpace(self,position):
        if(self.head is None):
            raise ("List of free Space is empty [Memory is full]")
        if(self.head.hasTheSamePosition(position)):
            self.head = self.head.getNextNode()
            return
        previousFreeSpaceNode = self.head
        for freeSpaceNode in self:
            if freeSpaceNode.hasTheSamePosition(position):
                previousFreeSpaceNode.setNextNode(freeSpaceNode.getNextNode())
                return
            previousFreeSpaceNode = freeSpaceNode
        raise Exception("No node with position '%s' not found" % position)

