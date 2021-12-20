from brownie import SimpleStorage, accounts
from brownie.network import account

# use -k "TestName" in order to test a single test
# use -pdb and upon failure
# -s to give good output
# go to pytest in order to check the docs


def test_deploy():
    # arrange
    account = accounts[0]
    # act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # assert
    assert starting_value == expected


def test_updating_storage():
    # arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # act
    expected = 15
    simple_storage.store(expected)
    actual = simple_storage.retrieve()
    # assert
    assert expected == actual
