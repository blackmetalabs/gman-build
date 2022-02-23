//pragma solidity ^0.8.0;
//
//
//import Ownable from './BMMultipass.sol';
//
///**
// * @title Whitelist
// * @dev The Whitelist contract has a whitelist of addresses, and provides basic authorization control functions.
// * @dev This simplifies the implementation of "user permissions".
// */
//contract Whitelist is Ownable {
//    mapping(address => uint256) public whiteList;
//    uint256 public whiteListCount;
//
//    /**
//     * @dev Adds an array of addresses to whitelist
//     * @param _whiteListAdditions array of addresses to add. Ignores doubles.
//     */
//    function addToWhiteList(address[] calldata _whiteListAdditions) external onlyOwner {
//        whiteListCount += 1; // Never decreases, even if address is removed from whitelist
//        for(uint256 i; i < _whiteListAdditions.length; i++){
//            if(whiteList[_whiteListAdditions[i]]==0){
//                whiteList[_whiteListAdditions[i]] = whiteListCount; // this number gives special treatment to first x on whitelist--OG
//            }
//        }
//    }
//
//    /**
//     * @dev Removes an array of addresses to whitelist
//     * @param _whiteListSubtractions array of addresses to remove. Ignores doubles.
//     */
//    function removeFromWhiteList(address[] calldata _whiteListSubtractions) external onlyOwner {
//      for(uint256 i; i < _whiteListSubtractions.length; i++){
//          if(whiteList[_whiteListSubtractions[i]]!=0){
//              whiteList[_whiteListSubtractions[i]] = 0;
//          }
//      }
//    }
//
//    function isWhitelisted(address _addy) external view returns(bool) {
//        return whiteList[_addy] > 0;
//    }
//
//    function whiteListPosition(address _addy) external view returns(uint256){
//        return whiteList[_addy];
//    }
//
//}