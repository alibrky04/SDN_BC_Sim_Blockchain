#########################################
# Class structure of blocks in blockchain
#########################################

import hashlib
import datetime         

class Block:
    def __init__(self, index, previous_hash, data, p_slots, nonce = 0, timestamp = str(datetime.datetime.now()), s_hash = None):
        self.index = index
        self.previous_hash = previous_hash
        self.data = data
        self.p_slots = p_slots
        self.nonce = nonce
        self.timestamp = timestamp
        self.mroot = self.calculate_mroot()
        if s_hash:
            self.hash = s_hash
        else:
            self.hash = self.calculate_hash()
        
    def calculate_mroot(self):
        return hashlib.sha256(str(self.data).encode()+str(self.p_slots).encode()).hexdigest()

    def calculate_hash(self):
        hash_string = str(self.previous_hash) + str(self.timestamp) + str(self.nonce) + str(self.data)
        return hashlib.sha256(hash_string.encode()).hexdigest()

    def get_index(self):
        return self.index

    def get_hash(self):
        return self.hash

    def get_previous_hash(self):
        return self.previous_hash

    def get_data(self):
        return self.data
    
    def get_p_slots(self):
        return self.p_slots

    def get_timestamp(self):
        return self.timestamp

    def get_nonce(self):
        return self.nonce