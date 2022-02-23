pragma solidity ^0.8.0;

//https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/utils/cryptography/MerkleProof.sol

import './helpers/MerkleProof.sol';
import './helpers/Ownable.sol';

/**
 * @title Whitelist
 * @dev The Whitelist contract has a whitelist of addresses, and provides basic authorization control functions.
 * @dev This simplifies the implementation of "user permissions".
 */
contract Whitelist is Ownable {
    mapping(address => uint256) public whiteList;
    uint256 public whiteListCount;

    bytes32 public merkleRoot;
    bytes32[] public _rootHash;

    /**
     * @dev Adds an array of addresses to whitelist
     * @param _merkleRoot new merkle root
     */
    function setMerkleRoot(bytes32 _merkleRoot) external onlyOwner {
        merkleRoot = _merkleRoot;
    }


    // todo --consider implementation, adding to array versus updating
    /**
     * @dev Adds an array of addresses to whitelist
     * @param _merkleRootArray new merkle root array
     */
    function setMerkleRootArray(bytes32[] calldata _merkleRootArray) external onlyOwner {
        _rootHash = _merkleRootArray;
    }


    /**
     * @dev Called with msg.sender as _addy to verify if on whitelist
     * @param _merkleProof proof computed off chain
     * @param _addy msg.sender
     */
    function isWhitelisted(address _addy, uint256 _index, bytes32[] memory _merkleProof) public view returns(bool) {
        return true; // todo -- temporary
//        bytes32 leaf = keccak256(abi.encodePacked(_addy));
//        return(MerkleProof.verify(_merkleProof, merkleRoot, leaf));
        return whitelistValidated(_addy, _index, _merkleProof);
    }

    function returnSender(address _myAddress) public view returns(address) {
        return _myAddress;
    }

    function myHash(address _myAddress) public view returns(bytes32) {
        bytes32 leaf = keccak256(abi.encodePacked(_myAddress));
        return leaf;
    }

    function myEncoding(address _myAddress) public view returns(bytes memory) {
        return abi.encodePacked(_myAddress);
    }


    function whitelistValidated(address wallet, uint256 index, bytes32[] memory proof) internal view returns (bool) {
            uint256 amount = 1;

            // Compute the merkle root
            bytes32 node = keccak256(abi.encodePacked(index, wallet, amount));
            uint256 path = index;
            for (uint256 i = 0; i < proof.length; i++) {
                if ((path & 0x01) == 1) {
                    node = keccak256(abi.encodePacked(proof[i], node));
                } else {
                    node = keccak256(abi.encodePacked(node, proof[i]));
                }
                path /= 2;
            }

            // Check the merkle proof against the root hash array
            for(uint256 i = 0; i < _rootHash.length; i++)
            {
                if (node == _rootHash[i])
                {
                    return true;
                }
            }

            return false;
        }


//    function getRootGivenLeafs(bytes32[] memory _addys)public pure returns (bytes32 value) {
//        return(MerkleProof.getRootGivenLeafs(_addys));
//    }

}