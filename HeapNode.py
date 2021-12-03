class HeapNode:
    key = ''
    valeu = 0
    position = 0
    freeBlocks = 0
    nextNode = None

    def __init__(self, key, valeu,position,freeBlocks):
        self.key=key
        self.valeu=valeu
        self.position =position
        self.freeBlocks = freeBlocks
    
    def setPosition(self,position):
        self.position=position
    def getPositin(self):
        return self.position
    
    def setFreeBlocks(self,freeBlocks):
        self.freeBlocks=freeBlocks

    def getFreeBlocks(self):
        return self.freeBlocks
    
    def getKey(self):
        return self.key

    def setKey(self,key):
         self.key =key

    def getValeu(self):
        return self.valeu

    def setValeu(self,valeu):
        self.valeu= valeu

    def getNextNode(self):
        return self.nextNode

    def setNextNode(self,nextNode):
        self.nextNode= nextNode

    def hasTheSamePosition(self,position):
        return self.position == position