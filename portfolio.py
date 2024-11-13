import requests
class StockPortfolio:
    def __init__(self, api_key):
        self.api_key = api_key
        self.portfolio = {}

    def add_stock(self, symbol, shares):
        if symbol in self.portfolio:
            self.portfolio[symbol] += shares
        else:
            self.portfolio[symbol] = shares
        print(f"Added {shares} shares of {symbol}.")

    def remove_stock(self, symbol, shares):
        if symbol in self.portfolio:
            if self.portfolio[symbol] >= shares:
                self.portfolio[symbol] -= shares
                if self.portfolio[symbol] == 0:
                    del self.portfolio[symbol]
                print(f"Removed {shares} shares of {symbol}.")
            else:
                print("Error: Not enough shares to remove.")
        else:
            print("Error: Stock not found in portfolio.")

    def get_stock_price(self, symbol):
        url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={self.api_key}"
        response = requests.get(url)
        data = response.json()
        try:
            price = float(data["Global Quote"]["05. price"])
            return price
        except KeyError:
            print("Error fetching data. Please check the stock symbol.")
            return None

    def track_performance(self):
        total_value = 0
        for symbol, shares in self.portfolio.items():
            price = self.get_stock_price(symbol)
            if price is not None:
                total_value += price * shares
                print(f"{shares} shares of {symbol} at ${price:.2f} each")
        
        print(f"Total portfolio value: ${total_value:.2f}")

def main():
    api_key = "YOUR_API_KEY"  # Replace with your Alpha Vantage API key
    tracker = StockPortfolio(api_key)

    while True:
        print("\n1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Performance")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            tracker.add_stock(symbol, shares)
        elif choice == '2':
            symbol = input("Enter stock symbol: ").upper()
            shares = int(input("Enter number of shares: "))
            tracker.remove_stock(symbol, shares)
        elif choice == '3':
            tracker.track_performance()
        elif choice == '4':
            print("Exiting the tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
