from Crypto.Hash import SHA256, keccak
from perkle import MerkleTree
from binascii import hexlify


# data_list = [b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9']
# sha256 = lambda x : SHA256.new(x).digest()
# mt = MerkleTree(data_list, sha256, random_padding=False, padding_byte=b'0')
# print(hexlify(mt.root()))
#

# def sha256(x):
#     return SHA256.new(x).digest()


# def get_root(data_list):
#     # data_list = [bin(x) for x in list]
#     # print(data_list)
#     bytes_list = [str.encode(x) for x in data_list]
#     sha256 = lambda x : SHA256.new(x).digest()
#     mt = MerkleTree(bytes_list, sha256, random_padding=False, padding_byte=b'0')
#     return hexlify(mt.root())


def hash_with_keccak(x):
    if type(x) == str:
        x = str.encode(x)
    keccak_hash = keccak.new(digest_bits=256)
    keccak_hash.update(x)
    return keccak_hash.hexdigest()


def get_root(data_list):
    # data_list = [bin(x) for x in list]
    # print(data_list)
    bytes_list = [str.encode(x) for x in data_list]
    mt = MerkleTree(bytes_list, hash_with_keccak, random_padding=False, padding_byte=b'0')
    return mt.root()


def hash_string(my_string):
    sha256 = lambda x: SHA256.new(x).digest()
    return hexlify(sha256(str.encode(my_string))).decode("utf-8")


def get_tree_object(data_list):
    bytes_list = [str.encode(x) for x in data_list]
    mt = MerkleTree(bytes_list, hash_with_keccak, random_padding=False, padding_byte=b'0')
    return mt


def get_proof(data_list, leaf):
    mt = get_tree_object(data_list)

    encoded_leaf = str.encode(leaf)
    index, proof_hashes = mt.proof(encoded_leaf)
    return index, proof_hashes


def compare(data_list):
    print(f'original: {data_list}')
    # p1 = get_proof(data_list, data_list[0])
    # p2 = get_proof_as_strings(data_list, data_list[0])
    # print(f'proof 1: {p1}')
    # print(f'proof 2: {p2}')
    # print(f'hashed: {hash_string(data_list[0])}')
    print(f'keccacked:')
    for x in data_list:
        print(f'{x}  ==>  {hash_with_keccak(x)}')

    print(f'get_root: {get_root(data_list)}')


def test_on_merkle(data_list):
    mt = get_tree_object(data_list)
    leaf = str.encode(data_list[0])
    passed = True

    # test 2
    failed = False
    try:
        index, proof_hashes = mt.proof(leaf)
        result = MerkleTree.verify(leaf, index, proof_hashes, mt.root(), hash_with_keccak)
    except Exception as e:
        failed = True
        print(f'failed with exception: {e}')
    assert failed == False, "Did not detect true leaf"

    passed = failed == False

    # test 2
    failed = False
    leaf = str.encode('0x6ADe6a2FFFFFFFFFFFFFFFFFFF')
    try:
        index, proof_hashes = mt.proof(leaf)
        result = MerkleTree.verify(leaf, index, proof_hashes, mt.root(), hash_with_keccak)
    except Exception as e:
        failed = True
        # print(f'failed with exception: {e}')
    assert failed == True, "Did not detect FALSE leaf"

    passed = failed and passed

    return passed


# data_list = ['0xa9fB5C3F2fD89122b1da1C1e7245f6ED5732B881', '0x6ADe6a2BDfBDa76C4555005eE7Dd7DcDE571D2a8']
# data_list = ['0x0063046686E46Dc6F15918b61AE2B121458534a5', '0x6ADe6a2BDfBDa76C4555005eE7Dd7DcDE571D2a8','0x66ab6d9362d4f35596279692f0251db635165871,']
# print(f'keccaked first element: {hash_with_keccak(data_list[0])}')
# compare(data_list)
# print(f'\ntesting....')
# test_on_merkle(data_list)
# res = test_on_merkle(data_list)
# print(f'res: {res}')
# #
