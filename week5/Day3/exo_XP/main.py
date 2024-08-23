class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __repr__(self):
        return(str(self.amount)+" " + self.currency)
         
    
c1=Currency("dollar",5)
print((c1))