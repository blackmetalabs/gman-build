#!/usr/bin/python3
from brownie import BMMultipass, Token, NTCitizenDeploy, accounts, network, config


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    print(network.show_active())
    # publish_source = True if os.getenv("ETHERSCAN_TOKEN") else False # Currently having an issue with this
    publish_source = False

    # deploy token
    token = Token.deploy("Fake Bytes", "FB", 18, 1e21, {'from': accounts[0]})

    ntc = NTCitizenDeploy.deploy({'from': accounts[0]})
    # function createCitizen(uint256 identityId, uint256 vaultId, uint256 itemCacheId, uint256 landDeedId, bool genderFemale, string memory specialMessage) public nonReentrant {


    # Deploy (call constructor)
    mp = BMMultipass.deploy(
        # config["networks"][network.show_active()]["vrf_coordinator"],
        # config["networks"][network.show_active()]["link_token"],
        # config["networks"][network.show_active()]["keyhash"],
        # {"from": dev},
        token.address,
        ntc.address,
        {"from": accounts[0]},
        publish_source=publish_source,
    )


    # bitPackingSuccessful = mp.verifyPacking();#[accounts[0]], {'from': accounts[0]})
    # print(f'Packing Successful: {bitPackingSuccessful}')
    #
    # availableClearanceLevels = mp.getAvailableClearanceLevelsGivenBytes(25);
    # print(f'Available Clearnce levels: {availableClearanceLevels}')



    tx = mp.addToWhiteList([accounts[0]], {'from': accounts[0]})


    for i in range(1):
        # // create a citizen with citizen Id=1, identityId=4 ,...
        tx = ntc.createCitizen(4, 5, 6, 7, False, "my special message goes here", {'from': accounts[0]})
        tx.wait(1)

        tx = token.approve(mp.address, 25, {'from': accounts[0]})
        tx.wait(1)
        tx = mp.claim(25, 1 + i, {'from': accounts[0], 'value': 10**13})
        tx.wait(1)

        uri = mp.tokenURI(i);
        print(f'uri:\n\n{uri}\n\n')

    # withdraw Bytes
    # print(f'Bytes Before: {token.balanceOf(accounts[0])}')
    # tx = mp.withdrawBytes(accounts[0].address, {'from': accounts[0]})
    # tx.wait(1)
    # print(f'Bytes After: {token.balanceOf(accounts[0])}')

    # withdraw ETH
    # print(f'Eth Balance Before: {mp.balance()}')
    # tx = mp.withdrawEth(accounts[0].address, {'from': accounts[0]})
    # print(f'Eth Balance After: {mp.balance()}')
    # tx.wait(1)


    return mp
