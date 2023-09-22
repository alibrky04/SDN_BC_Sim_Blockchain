"""
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
"""
        
        
##########################
# Test code for blockchain
##########################

from block import Block
from blockchain import Blockchain
from consensus import Consensus
import random
import time

#a list to keep track of the available hosts
AvailableHosts = list(range(10))

#Start the timer
StartTime = time.time()

new_blockchain = Blockchain()
new_consensus = Consensus(3)

#Create a host class
class Host:
    def __init__(self, HostNumber, SwitchNumber, RemoveTime):
        self.HostNumber = HostNumber
        self.SwitchNumber = SwitchNumber
        self.RemoveTime = RemoveTime
        
    def __str__(self):
        return (f"Host:{self.HostNumber} Switch:{self.SwitchNumber} Removal Time: {self.RemoveTime}")        
HostList = [Host(-1, 0, 9999) for _ in range(0)]
  
  
#Function to recieve the uptime of the program
def GetUpTime():
    global StartTime
    Uptime = time.time() - StartTime
    return int(Uptime)
 
#Create a number that will count as a time slot's length of time. 
def SetTimeSlot():
    TimeSlot = random.randint(6, 12)
    return TimeSlot
    
#Set the time that the host will be removed.     
def SetRemoveTime(TimeSlot, Uptime):
    RemoveTime = TimeSlot + Uptime
    return RemoveTime
    
#Create a number to represent the hosts.
def SetHostNumber():
    if not AvailableHosts:
        print("There is no more room for any hosts.")
        return None
    HostNumber = random.choice(AvailableHosts)
    AvailableHosts.remove(HostNumber)
    return HostNumber

#Assign a switch to each host.
def SetSwitchNumber(HostNumber):
    SwitchNumber = int
    if HostNumber is not None:
        if HostNumber <= 15:
            SwitchNumber = 1
        elif HostNumber <= 30:
            SwitchNumber = 2
        elif HostNumber > 30:
            SwitchNumber = 3
    return SwitchNumber

#Remove a host and return the number to the list.
def RemoveHostNumber(HostNumber):
    if HostNumber is not None:
        AvailableHosts.append(HostNumber)
        
#Simulate hosts joining and leaving.        
def SimulateHost():
    global HostList
    HostNumber = SetHostNumber()
    ListLength = len(HostList) 
    Uptime = GetUpTime()
    if HostNumber is not None:
        NewHost = Host(HostNumber, SetSwitchNumber(HostNumber), SetRemoveTime(SetTimeSlot(), Uptime))
        HostList.append(NewHost)
        print(NewHost, "Current Time: ", Uptime) 
        print("Before generateNewBlock:", HostNumber)
        new_block = new_consensus.generateNewBlock(new_blockchain.getLastBlock(), HostNumber, True)
        print("After generateNewBlock:", HostNumber)
        if new_block:
            new_blockchain.addBlock(new_block)
        else:
            print("Failed to create a new block.")
    else:
        print("No new hosts can be added until there is an open IP")
    for i in range (0, ListLength-1):
        if i > ListLength - 1:
            i = ListLength-1
        if HostList[i].RemoveTime <= Uptime:
            RemoveHostNumber(HostList[i].HostNumber) 
            print(HostList[i].HostNumber, "Has Been Removed")
            new_block = new_consensus.generateNewBlock(new_blockchain.getLastBlock(), HostNumber, False)
            new_blockchain.addBlock(new_block)
            HostList.remove(HostList[i]) 
            ListLength -= 1

if __name__ == "__main__":
    while GetUpTime() <= 20:
        time.sleep(1)
        SimulateHost()
        
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
        