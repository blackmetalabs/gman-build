import hashlib
import binascii
from Crypto.Hash import keccak

# k = keccak.new(digest_bits=256)
# k.update('age')
# print
# k.hexdigest()

def hashIt(firstTxHash, secondTxHash):
    # Reverse inputs before and after hashing
    # due to big-endian
    unhex_reverse_first = binascii.unhexlify(firstTxHash)[::-1]
    unhex_reverse_second = binascii.unhexlify(secondTxHash)[::-1]

    concat_inputs = unhex_reverse_first + unhex_reverse_second
    first_hash_inputs = hashlib.sha256(concat_inputs).digest()
    final_hash_inputs = hashlib.sha256(first_hash_inputs).digest()
    # reverse final hash and hex result
    return binascii.hexlify(final_hash_inputs[::-1])


# Hash pairs of items recursively until a single value is obtained
def merkleCalculator(hashList):
    if len(hashList) == 1:
        return hashList[0]
    newHashList = []
    # Process pairs. For odd length, the last is skipped
    for i in range(0, len(hashList) - 2):
        newHashList.append(hashIt(hashList[i], hashList[i + 1]))
    if len(hashList) % 2 == 1:  # odd, hash last item twice
        newHashList.append(hashIt(hashList[-1], hashList[-1]))
    return merkleCalculator(newHashList)


# Demo :
# https://blockexplorer.com/block/000000000003ba27aa200b1cecaad478d2b00432346c3f1f3986da1afd33e506
# print('Expected MerkleRoot :   f3e94742aca4b5ef85488dc37c06c3282295ffec960994b2c0d5ac2a25a95766')
#
# Transaction Hashes of block #100000
txHashes = [
    '33A4622B82D4c04a53e170c638B944ce27cffce3',
    '33A4622B82D4c04a53e170c638B944ce27cffce3',
    '6359f0868171b1d194cbee1af2f16ea598ae8fad666d9b012c8ed2b79a236ec4',
    'e9a66845e05d5abc0ad04ec80f774a7e585c6e8db975962d069a522137b80c1d'
]

CalculatedMerkleRoot = str(merkleCalculator(txHashes), 'utf-8')
print('Calculated MerkleRoot : ' + CalculatedMerkleRoot)


def get_root_given_array(hashlist):
    return str(merkleCalculator(hashlist), 'utf-8')
