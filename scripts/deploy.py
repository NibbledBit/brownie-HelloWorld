from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    print(f"Account: {account}")
    print("Deploying...")
    simple_storage = SimpleStorage.deploy({"from": account})
    print("Deployed SimpleStorage")
    print(f"{simple_storage}")
    stored_value = simple_storage.retrieve()
    print(f"Current Stored Value: {stored_value}")
    print("Updating Stored Value...")
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(f"Updated Stored Value: {updated_stored_value}")


# account = accounts.load("shauns-account")
# print(account)
# account = accounts.add(config["wallets"]["from_key"])
# print(account)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
