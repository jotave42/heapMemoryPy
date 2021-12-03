
from LinkedList import LinkedList
from HeapNode import HeapNode
class HeapMemory:
    size = 30
    heapArray = [False] * size
    heapArrayValues  =  ['*'] * size
    freeSpaceList = LinkedList(size)
    node=None
    index ={}
    method =''
    commands=''
    def __init__(self, commands):
        self.commands = commands
        with open(self.commands,'r') as commandslist:
            commandsToExecute = commandslist.readlines()
            for commandToExecute in commandsToExecute:
    
                print('command To Execute => %(command)s ' % {"command": commandToExecute})
                commandAndParams = commandToExecute.strip()
                params = commandAndParams.split()
                if(params[0] == 'exibe'):
                    self.showHeap()
                elif(params[0] == 'heap'):
                    self.method = params[1]
                elif(params[0] == 'del'):
                    if(self.hasDuplicate( self.index[params[1]])):
                        position = self.index[params[1]]
                        self.index.pop(list(self.index.keys())[list(self.index.values()).index(position)])
                    self.removeBlock(self.index[params[1]])
                elif(params[0] == 'new'):
                    if(self.method=='wrost'):
                        self.index[params[1]] = self.worstFit(int(params[2]))
                    if(self.method == 'best'):
                        self.index[params[1]] = self.bestFit(int(params[2]))
                    self.setHeap(self.index[params[1]],int(params[2]),params[1])
                elif(params[1]== '='):
                    self.index[params[0]] = int(self.index[params[2]])



    def bestFit(self,blocksCount):
        smallestFreeSpace = self.freeSpaceList.head.getFreeBlocks()
        position = self.freeSpaceList.head.getPosition()
        for nodeFreeSpace in self.freeSpaceList:
            if (blocksCount <= nodeFreeSpace.getFreeBlocks() <=  smallestFreeSpace):
                smallestFreeSpace = nodeFreeSpace.getFreeBlocks()
                position = nodeFreeSpace.getPosition()
        for nodeFreeSpace in self.freeSpaceList:
            if(nodeFreeSpace.hasTheSamePosition(position)):
                nodeFreeSpace.setPosition(nodeFreeSpace.getPosition()+blocksCount)
                nodeFreeSpace.setFreeBlocks(nodeFreeSpace.getFreeBlocks()-blocksCount)
                if(nodeFreeSpace.getFreeBlocks()==0):
                    self.freeSpaceList.removeFromFreeSpace(nodeFreeSpace.getPosition())
                return position
                

    def worstFit(self,blocksCount):
        largestFreeSpace = self.freeSpaceList.head.getFreeBlocks()
        position = self.freeSpaceList.head.getPosition()
        for nodeFreeSpace in self.freeSpaceList:
            if ((nodeFreeSpace.getFreeBlocks()> largestFreeSpace) and (blocksCount <= nodeFreeSpace.getFreeBlocks())):
                 largestFreeSpace = nodeFreeSpace.getFreeBlocks()
                 position = nodeFreeSpace.getPosition()
        for nodeFreeSpace  in self.freeSpaceList:
            if (nodeFreeSpace.hasTheSamePosition(position)):
                nodeFreeSpace.setPosition(nodeFreeSpace.getPosition()+blocksCount)
                nodeFreeSpace.setFreeBlocks(nodeFreeSpace.getFreeBlocks()-blocksCount)
                if (nodeFreeSpace.getFreeBlocks()==0):
                    self.freeSpaceList.removeFromFreeSpace(nodeFreeSpace.getPosition())
                print(nodeFreeSpace.getPrintableFreeBlocksList())
                return position
   


    def setHeap(self, position, blocks,value):
        for i in range(position, position+blocks):
            self.heapArray[i] = True
            self.heapArrayValues[i] = value
    
    def hasDuplicate(self, value):
        countTotal = 0
        for numberOfBlocks in self.index.values():
            if numberOfBlocks == value:
                countTotal += 1
        return countTotal > 1

    def removeBlock(self,blcokIndex):
        if( (self.hasSpaceBeforeEnd(blcokIndex)) and (self.hasSpaceBefore(blcokIndex))):
            for nodeFreeSpace  in self.freeSpaceList:
                if(nodeFreeSpace.getNextNode().getPosition()>blcokIndex):
                    nodeFreeSpace.setFreeBlocks(self.getNextIndexPosintion(blcokIndex)-blcokIndex)
                    if(nodeFreeSpace.getNextNode() is not None):
                        nodeFreeSpace.setNextNode(nodeFreeSpace.getNextNode().getNextNode())
        elif( (not self.hasSpaceAftherEnd(blcokIndex)) and ( self.hasSpaceBefore(blcokIndex) ) ):
            for nodeFreeSpace  in self.freeSpaceList:
                if(nodeFreeSpace.getNextNode().getPosition()>blcokIndex):
                    newNodeFreeSpace =HeapNode(None,None,blcokIndex,self.getNextIndexPosintion(blcokIndex)-blcokIndex)
                    newNodeFreeSpace.setNextNode(nodeFreeSpace.getNextNode())
                    nodeFreeSpace.setNextNode(newNodeFreeSpace)
        elif ( ( self.hasSpaceAfther(blcokIndex) ) and ( self.hasSpaceAftherEnd(blcokIndex) ) ):
            for nodeFreeSpace  in self.freeSpaceList:
                if (nodeFreeSpace.getPosition()<blcokIndex):
                    nodeFreeSpace.setPosition(blcokIndex)
                    nodeFreeSpace.setFreeBlocks(self.getNextIndexPosintion(blcokIndex)-blcokIndex)
        else:
            newNodeFreeSpace =HeapNode(None,None,blcokIndex,self.getNextIndexPosintion(blcokIndex)-blcokIndex)
            newNodeFreeSpace.setNextNode(self.freeSpaceList.getHead())
            self.freeSpaceList.setHead(newNodeFreeSpace)



    def hasSpaceBeforeEnd(self,indexPosition):
        for nodeFreeSpace  in self.freeSpaceList:
            if ( indexPosition == ( nodeFreeSpace.getFreeBlocks() + nodeFreeSpace.getPosition() ) ):
                return True
        return False

    def hasSpaceBefore(self,indexPosition):
        for nodeFreeSpace  in self.freeSpaceList:
             if( nodeFreeSpace.getPosition() <indexPosition):
                 return True
        return False
    
    def hasSpaceAftherEnd(self, indexPosition):
        for nodeFreeSpace  in self.freeSpaceList:
             if(indexPosition < nodeFreeSpace.getPosition() <self.getNextIndexPosintion(indexPosition) ):
                 return True
        return False
    def hasSpaceAfther(self,indexPosition):
        for nodeFreeSpace  in self.freeSpaceList:
             if( indexPosition == ( nodeFreeSpace.getFreeBlocks()+nodeFreeSpace.getPosition())):
                 return True
        return False


        
            


    def getNextIndexPosintion(self,indexPosition):
        positionsSorted = sorted(self.index.values())
        if( (len(positionsSorted) -1) ==positionsSorted.index(indexPosition) ):
            return self.size
        else:
            for i, val in enumerate(positionsSorted[:-1]):
                if val ==indexPosition:
                    return positionsSorted[i+1]
        


    def showHeap(self):
        print('===============SHOWING HEAP======================')
        print("|position || In Use |")
        for indexOfHeap,value in enumerate(self.heapArray): 
            print('|%(index)d || %(inUse)s |' % {"index": indexOfHeap,'inUse':value,'value':self.heapArrayValues[indexOfHeap]})
        print("===========LIST OF FREE SPACE============")
        print(self.freeSpaceList.getPrintableFreeBlocksList())
        print('=========END OF SHOWING HEAP======================')