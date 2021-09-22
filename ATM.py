class ATM:
    def __init__(self,atmCardNumber,pinNumber,CashWithdrawl,BalanceEnquiry):
        self.atmCardNumber = atmCardNumber
        self.pinNumber = pinNumber
        self.CashWithdrawl = CashWithdrawl
        self.BalanceEnquiry = BalanceEnquiry   
        


    def setPrice(self):
        print(self.atmCardNumber)  
        print(self.pinNumber)
        print(self.CashWithdrawl)
        print(self.BalanceEnquiry)

atm1 = ATM(102065, 5204, 5000, 500000)
atm1.setPrice()