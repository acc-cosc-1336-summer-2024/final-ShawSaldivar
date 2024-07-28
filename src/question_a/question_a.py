#write functions here, don't add input('') statements here!
def test_config():
    return True

class Stock:

    def __init__(self):
        self.symbol = ""
        self.company_name = ""
        

    def symbol(self):
        return self.symbol
    def company_name(self):
        return self.company_name
    
    def stock_purchase_history(self):
        StockDict = {}
        StockDict["AAPL"] = "Apple Inc"
        StockDict["CAT"] = "Caterpillar"
        StockDict["EK"] = "Eastman Kodak"
        StockDict["GOOG"] = "Google"
        StockDict["MSFT"] = "Microsoft"
        
        for Keys, Values in StockDict.items():
            print(Keys," | ",Values)