import yfinance as yf

# A dictionary to hold the stock portfolio
portfolio = {}

def add_stock(symbol, shares):
    """Add stock to the portfolio."""
    if symbol in portfolio:
        portfolio[symbol] += shares
    else:
        portfolio[symbol] = shares
    print(f"Added {shares} shares of {symbol}.")

def remove_stock(symbol, shares):
    """Remove stock from the portfolio."""
    if symbol in portfolio and portfolio[symbol] >= shares:
        portfolio[symbol] -= shares
        print(f"Removed {shares} shares of {symbol}.")
        if portfolio[symbol] == 0:
            del portfolio[symbol]
    else:
        print(f"Not enough shares of {symbol} to remove.")

def view_portfolio():
    """View the portfolio and get current stock prices."""
    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("\nYour Stock Portfolio:")
    total_value = 0

    for symbol, shares in portfolio.items():
        stock = yf.Ticker(symbol)
        current_price = stock.history(period="1d")['Close'][0]
        stock_value = shares * current_price
        total_value += stock_value
        print(f"{symbol}: {shares} shares at ${current_price:.2f} each, Total: ${stock_value:.2f}")
    
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Main menu loop
def portfolio_tracker():
    while True:
        print("\nPortfolio Tracker Menu")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input(f"Enter number of shares to add for {symbol}: "))
            add_stock(symbol, shares)

        elif choice == '2':
            symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
            shares = int(input(f"Enter number of shares to remove for {symbol}: "))
            remove_stock(symbol, shares)

        elif choice == '3':
            view_portfolio()

        elif choice == '4':
            print("Exiting Portfolio Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the portfolio tracker
portfolio_tracker()
