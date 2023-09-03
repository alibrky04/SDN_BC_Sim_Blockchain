#####################################################
# Class structure and functions of consensus protocol
#####################################################

from block import Block
from blockchain import Blockchain
import hashlib
import datetime

# Takes a parameter for diffucilty level in integer
class Consensus:
    def __init__(self, difficulty):
        self.difficulty = difficulty # Diffucilty level of consensus
        self.MAX_NONCE = 2 ** 32 # Max value for nonce
        self.target = "0" * self.difficulty # Number of 0's from the left in the hash
        
    # First parameter is the previous block, second parameter is the data that block will hold and the third paramter is a boolean for entering or exiting status
    # True is enter and False is exit
    def PoW(self, prevBlock, data, enter):
        p_slots = prevBlock.get_p_slots().copy() # Gets a copy of the previous blocks parking slots
        mroot = hashlib.sha256(str(data).encode() + str(p_slots).encode()).hexdigest() # Merkle root of the complete data
        timestamp = str(datetime.datetime.now())
        nonce = 0
        c_header = mroot + timestamp + str(prevBlock.hash) # Total variable for all of the data
        if enter:
            if p_slots[data] == 0: # If the parking slot is free, It makes that parking slot full
                p_slots[data] = 1
                
                # It finds the correct hash for the block
                for nonce in range(self.MAX_NONCE):
                    hash_result = hashlib.sha256(str(c_header).encode() + str(nonce).encode()).hexdigest()
                    if hash_result[:self.difficulty] == self.target:
                        return hash_result, data, p_slots, timestamp, nonce
            return False, data, p_slots, timestamp, nonce
        else:
            if p_slots[data] == 1: # If the parking slot is full, It makes that parking slot free
                p_slots[data] = 0
                
                # It finds the correct hash for the block
                for nonce in range(self.MAX_NONCE):
                    hash_result = hashlib.sha256(str(c_header).encode() + str(nonce).encode()).hexdigest()
                    if hash_result[:self.difficulty] == self.target:
                        return hash_result, data, p_slots, timestamp, nonce
            return False, data, p_slots, timestamp, nonce
    
    def generateNewBlock(self, prevBlock, data, enter):
        new_hash, data1, p_slots, timestamp, nonce = self.PoW(prevBlock, data, enter)
        new_p_slots = p_slots.copy()
        if enter:
            if new_hash:
                return Block(prevBlock.index + 1, prevBlock.hash, data1, new_p_slots, nonce, timestamp, new_hash)
            next_block = prevBlock
            next_block.previous_hash = prevBlock.hash
            next_block.hash = None
            next_block.timestamp = str(datetime.datetime.now())
            next_block.nonce = 0
            return next_block
        else:
            if new_hash:
                return Block(prevBlock.index + 1, prevBlock.hash, data1, new_p_slots, nonce, timestamp, new_hash)
            next_block = prevBlock
            next_block.previous_hash = prevBlock.hash
            next_block.hash = None
            next_block.timestamp = str(datetime.datetime.now())
            next_block.nonce = 0
            return next_block

        
def is_valid(self, bc):
        for i in range(1, len(bc)):
            current_block = bc[i]
            previous_block = bc[i - 1]
            if current_block.get_hash() != current_block.calculate_hash():
                return False
            elif current_block.get_previous_hash() != previous_block.get_hash():
                return False
            elif previous_block.p_slots[current_block.data] != 0:
                return False
        return True