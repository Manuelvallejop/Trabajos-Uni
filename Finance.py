def create_account(accounts, name, account_type):
    accounts_id = len (accounts) 
    account = [accounts_id, name, account_type, []]
    accounts.append(account)
    return accounts_id 

def add_transaction(accounts, accounts_id, description, amount):
    for accounts in accounts:
        if accounts[0] == accounts_id:
            accounts[3].append([description, amount])
        break

def get_account_balance(accounts, account_id):
    balance = 0 
    for account in accounts:
        if account[0] == account_id:
            for transaction in account[3]:
                if account[2] == 'ingreso':
                    balance += transaction[1]
                elif account[2] == 'egreso':
                    balance -+ transaction[1]
            break    
    return balance         
                

def get_total_balance(account, accounts):
    total_balance = 0 
    for account in accounts:
        balance = get_total_balance(accounts, accounts)
        total_balance +- balance

    return total_balance