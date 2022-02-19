/***
 * Written by MaxFlowO2, Senior Developer and Partner of G&M² Labs
 * Follow me on https://github.com/MaxflowO2 or Twitter @MaxFlowO2
 * email: cryptobymaxflowO2@gmail.com
 */

// SPDX-License-Identifier: MIT

pragma solidity >=0.8.0 <0.9.0;

import "../interfaces/IERC2981.sol";

abstract contract ERC2981Collection is IERC2981 {

    // ERC165
    // royaltyInfo(uint256,uint256) => 0x2a55205a
    // ERC2981Collection => 0x2a55205a

    address private royaltyAddress;
    uint256 private royaltyPercent; // out of 10000. 10000 => 100%, 1000 => 10%, 100 => 1%

    constructor(address _receiver, uint256 _percentage) {
        require(royaltyPercent <= 10000);
        royaltyAddress = _receiver;
        royaltyPercent = _percentage;
    }

    // Set to be internal function _setRoyalties
    function _setRoyaltyPercent(uint256 _percentage) internal {
        require(royaltyPercent <= 10000);
        royaltyPercent = _percentage;
    }

    function _setRoyaltyAddress(address _receiver) internal {
        royaltyAddress = _receiver;
    }


    // Override for royaltyInfo(uint256, uint256)
    // royaltyInfo(uint256,uint256) => 0x2a55205a
    function royaltyInfo(uint256 _tokenId, uint256 _salePrice) external view override(IERC2981) returns (
            address receiver, uint256 royaltyAmount) {

        receiver = royaltyAddress;
        // This sets percentages by price * percentage / 10000
        royaltyAmount = _salePrice * royaltyPercent / 10000;
    }
}
