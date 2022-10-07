from LinkedList import LinkedList
class Bill:
    def __init__(self, value):
        self.value = value
        if value == 1:
            self.title = str(value) + " Dollar"
        else:
            self.title = str(value) + " Dollars"
        
    def __str__(self):
        return self.title

class CashRegister:
    def __init__(self):
        self.cr = LinkedList()
        self.total = 0
    
    def add_bill(self, bill):
        bill = Bill(bill)
        self.cr.add_first(bill)
    
    def change(self, price, bill):
        pass