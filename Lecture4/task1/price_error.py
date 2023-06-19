class PriceError(Exception):
    def __init__(self,price, msg):
        self.price = price
        self.msg = msg
