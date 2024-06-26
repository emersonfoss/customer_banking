class Account:
    def __init__(self, balance=0, interest_rate=0):
        self.balance = balance
        self.interest_rate = interest_rate
    
    def set_balance(self, balance):
        self.balance = balance
    
    def set_interest(self, interest_rate):
        self.interest_rate = interest_rate
    
    def calculate_interest(self, months):
        return self.balance * (self.interest_rate / 100) * (months / 12)

def create_savings_account(balance, interest_rate, months):
    account = Account(balance, interest_rate)
    interest_earned = account.calculate_interest(months)
    updated_balance = balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)
    return updated_balance, interest_earned

def create_cd_account(balance, interest_rate, months):
    account = Account(balance, interest_rate)
    interest_earned = account.calculate_interest(months)
    updated_balance = balance + interest_earned
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)
    return updated_balance, interest_earned

def main():
    # Prompt for savings account details
    savings_balance = float(input("Enter the initial balance for the savings account: "))
    savings_interest_rate = float(input("Enter the annual interest rate for the savings account (in %): "))
    savings_months = int(input("Enter the number of months the interest is applied to the savings account: "))

    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)
    print(f"Savings Account - Interest Earned: ${savings_interest_earned:.2f}, Updated Balance: ${updated_savings_balance:.2f}")

    # Prompt for CD account details
    cd_balance = float(input("Enter the initial balance for the CD account: "))
    cd_interest_rate = float(input("Enter the annual interest rate for the CD account (in %): "))
    cd_months = int(input("Enter the number of months the interest is applied to the CD account: "))

    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)
    print(f"CD Account - Interest Earned: ${cd_interest_earned:.2f}, Updated Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
