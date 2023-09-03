##########################
# Test code for blockchain
##########################

from block import Block
from blockchain import Blockchain
from consensus import Consensus

if __name__ == "__main__":
    new_blockchain = Blockchain()
    new_consensus = Consensus(3)
    
    num_blocks = 10 # Number of blocks to be added
    
    for i in range(0, num_blocks):
        new_block = new_consensus.generateNewBlock(new_blockchain.getLastBlock(), i, True)
        new_blockchain.addBlock(new_block)
        
    # Display the entire blockchain
    
    for i, block in enumerate(new_blockchain.getChain()):
        print(f"{i + 1}. Block")
        block_p_slots = block.get_p_slots().copy()
        print("Data:", block.get_data())
        for j in range(10):
            print(f"Parking Slot {j + 1}: {block_p_slots[j]}")
        print("Hash:", block.get_hash())
        print("Previous Hash:", block.get_previous_hash())
        print("Time:", block.get_timestamp())
        print("Nonce:", block.get_nonce(), "\n")
        