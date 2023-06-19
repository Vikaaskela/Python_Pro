#Task 2
#Створіть абстрактний базовий клас "ПлатіжнийЗасіб" з методом "здійснити_платіж()". Створіть підкласи 
#"КредитнаКарта", "БанківськийПереказ", "ЕлектроннийГаманець" і т.д., які успадковують цей метод та 
#реалізовують його відповідно до специфіки кожного платіжного засобу. Створіть клас "ПлатіжнийПроцесор", 
#який містить список доступних платіжних засобів та метод для виконання платежу через вибраний засіб. 
#Можна створити об'єкти різних платіжних засобів, додати їх до платіжного процесора і здійснити платежі через них

class PaymentInstrument:
    
    def make_payment(self):
        raise NotImplementedError
    
class CreditCard(PaymentInstrument):
    def make_payment(self):
        return 

    
class BankTransfer(PaymentInstrument):
    def make_payment(self):
        return 

    

class ElectronicWallet(PaymentInstrument):
    def make_payment(self):
        return 
    
class PaymentProcessor:

    
    
x = CreditCard()
y = BankTransfer()
z = ElectronicWallet()

print(x.make_payment())
print(y.make_payment())
print(z.make_payment())
