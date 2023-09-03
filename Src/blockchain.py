###################################
# Class structure of the blockchain
###################################

from block import Block
from collections import deque

class Blockchain:
    def __init__(self):
        self.chain = deque()
        genesis_block = Block(0,None,0,[0,0,0,0,0,0,0,0,0,0],0)
        self.chain.appendleft(genesis_block)

    def getChain(self):
        return self.chain
    
    def getLastBlock(self):
        return self.chain[-1]
    
    def addBlock(self, Block):
        self.chain.append(Block)