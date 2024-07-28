#write functions here, don't add input('') statements here!
class Stock:
    
    def __init__(self):
        self.symbol = ["AAPL","CAT","EK","GOOG","MSFT"]
        self.company_name = ["Apple Inc", "Caterpillar", "Eastman Kodak", "Google", "Microsoft"]

    def get_symbol(self,value):
        return (self.symbol[value])
    
    def get_company_name(self,value):
        return (self.company_name[value])
    