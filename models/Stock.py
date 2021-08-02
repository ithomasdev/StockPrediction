class Stock:
    def __init__(self, name, symbol, data):
        self.name = name
        self.symbol = symbol
        self.data = data

    # Sample methods, these would use the dataframe(data) to get values for specific dates     
    def get_open(self, date, symbol):
        open_price = symbol.loc[date].open
        return open_price

    def get_close(self, date, symbol):
        close_price = symbol.loc[date].close
        return close_price

    def get_high(self, date, symbol):
        high_price = symbol.loc[date].high
        return high_price

    def get_low(self, date, symbol):
        low_price = symbol.loc[date].low
        return low_price