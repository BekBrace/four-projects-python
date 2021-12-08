from hashlib import sha256

MAX_NONCE = 10000000000

# SHA256 is an algorithm for 
def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Cool! Succesfully mined bictoins with nonce value: {nonce}")
            return new_hash
     
    raise BaseException(f"Sorry! Could not find it after trying {MAX_NONCE} times")

# Main block
if __name__ == "__main__":
    transactions = '''
    Baldur->John->20
    Lara->Freya->45
    '''
    # Try to change this to higher number, and you see it will take more time for mining as difficulty level increases
    difficulty = 5
    import time
    start = time.time()
    print('Start mining ... ⛏️    ')
    
    new_hash = mine(6, transactions, 
                    'aded354032d0a8e9d9c51995ed73b5a056d5ffe6', difficulty)
    time_spent_on_mining = str((time.time() - start))
    print(f"Mining Terminated ⚒️  in {time_spent_on_mining} seconds.")
    print(new_hash)
    
    