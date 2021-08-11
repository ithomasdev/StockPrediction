class Stock:
    def __init__(self, name, symbol, data):
        self.name = name
        self.symbol = symbol
        self.data = data

    # Sample methods, these would use the dataframe(data) to get values for specific dates     
    def get_open(self, date):
        return self.data.loc[date].open

    def get_close(self, date):
        return self.data.loc[date].close

    def get_high(self, date):
        return self.data.loc[date].high

    def get_low(self, date):
        return self.data.loc[date].low
