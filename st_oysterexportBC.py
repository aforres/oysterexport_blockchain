import streamlit as st

st.subheader("How this all began")
st.markdown("""As a past Commodities Risk Analyst for the (then) New South Wales Department of Agriculture, I worked with farmers state-wide to hedge their produce price risk. Two decades on I was asked by a friend to build
a blockchain to monitor the export conditions and timing for a group of NSW oyster lease farmers who were looking at getting
fresh oysters to markets in Asia within the 48 hours time bracket in mint condition. Beneath is my simple solution - which you
can run by clicking the nearby button.
""")


code = """
#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
### OysterExportBC_00_002.py 
### Python 3.6.4 author: aforres@gmail.com 20180721
################################################################################

import hashlib as hashmake
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashmake.sha256()
        sha.update(str(self.index).encode('utf-8') +
                   str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') +
                   str(self.previous_hash).encode('utf-8'))
                   #Unicode-objects must be encoded before hashing 
        return sha.hexdigest()

def create_first_block():
    return Block(0, date.datetime.now(), "Start Block", "0")


def next_block(last_block):
    this_index = last_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

if __name__ == '__main__':

    ## Create the blockchain and add the first block
    blockchain = [create_first_block()]
    previous_block = blockchain[0]

    # Number of blocks we add to the chain
    num_of_blocks_to_append = 5

    # Add blocks to the chain
    print('Demo Lake to Plate grade Sydney Rock Oysters for premium export - blockchain tracking')
    v = [['123','0097','20180721_0832','20180721_1547'],['243','0016','20180721_0712','20180721_1547'],['148','0101','20180721_0910','20180721_1547'],['341','0003','20180721_0730','20180721_1547'],['123','1234','20180721_0832','20180721_1547']]
    for i in range(0, num_of_blocks_to_append):
        block_to_append = next_block(previous_block)
        blockchain.append(block_to_append)
        previous_block = block_to_append
        
        print("Block #{} added. Data: {} dozen, producer ID: {}, {} harvested, {} air_freighted.".format(block_to_append.index, v[i][0], v[i][1], v[i][2], v[i][3]))
        print("Hash: {}\n".format(block_to_append.hash))
"""

st.code(code, language="python")


#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
### OysterExportBC_00_002.py 
### Python 3.6.4 author: aforres@gmail.com 20180721
################################################################################

import streamlit as st
import hashlib as hashmake
import datetime as date

def run_all():

    class Block:
        def __init__(self, index, timestamp, data, previous_hash):
            self.index = index
            self.timestamp = timestamp
            self.data = data
            self.previous_hash = previous_hash
            self.hash = self.hash_block()

        def hash_block(self):
            sha = hashmake.sha256()
            sha.update(str(self.index).encode('utf-8') +
                       str(self.timestamp).encode('utf-8') +
                       str(self.data).encode('utf-8') +
                       str(self.previous_hash).encode('utf-8'))
                       #Unicode-objects must be encoded before hashing 
            return sha.hexdigest()

    def create_first_block():
        return Block(0, date.datetime.now(), "Start Block", "0")


    def next_block(last_block):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = str(this_index)
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

    ## Create the blockchain and add the first block
    blockchain = [create_first_block()]
    previous_block = blockchain[0]

    num_of_blocks_to_append = 5

    st.markdown('**Demo Lake to Plate grade Sydney Rock Oysters for premium export - blockchain tracking**')
    v = [['123','0097','20180721_0832','20180721_1437'],['243','0016','20180721_0712','20180721_1445'],['148','0101','20180721_0910','20180721_1507'],['341','0003','20180721_0730','20180721_1532'],['123','1234','20180721_0832','20180721_1547']]
    for i in range(0, num_of_blocks_to_append):
        block_to_append = next_block(previous_block)
        blockchain.append(block_to_append)
        previous_block = block_to_append
            
        st.markdown("Block #{} added. Data: {} dozen, producer ID: {}, {} harvested, {} air_freighted.".format(block_to_append.index, v[i][0], v[i][1], v[i][2], v[i][3]))
        st.markdown("Hash: {}\n".format(block_to_append.hash))
            
if __name__ == "__main__":
    if st.button("run blockchain"):
        run_all()
    
    
