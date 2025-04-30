print("Welcome to the Stock Market Simulator!")

name = input("What is your name? ")
print("Hello, " + name + "!")

should_we_trade = input("Do you want to play? (yes/no) ").lower()

if should_we_trade == 'yes':
    print("Welcome to the stock market simulator, here are the available stock holdings to choose from: ")
    print("QQQM, SCHD, PLTR, NVDA,")
elif should_we_trade == 'no':
    exit()
else:
    print("Invalid option. Please select again!")

stock_options = ['QQQM', 'SCHD', 'PLTR', 'NVDA']

current_stock_prices = {
    'QQQM': 195.48,
    'SCHD': 25.62,
    'PLTR': 109.56,
    'NVDA': 108.65,

}

print("Here are the current stock prices: ")
for stock, price in current_stock_prices.items():
    print(f"{stock}: ${price:.2f}")


option_1 = input("Which stock holding would you like to trade first today?").lower().upper()
if option_1 in stock_options:
    print(f"You have selected {option_1}. The current price is ${current_stock_prices[option_1]:.2f}.")
else:
    print("Invalid stock option. Please select a valid stock from the list!")

choice_1 = input("Are we buying or selling more shares today? (buying/selling) ")
if choice_1 == 'buying':
    print("We are buying more shares!")
    variation_1 = input("How many shares are we purchasing today? (1-1000) ")
    if 1 <= int(variation_1) <= 1000:
        print(f"We are purchasing {variation_1} shares of {option_1} at ${current_stock_prices[option_1]:.2f} each.")

elif choice_1 == 'selling':
    print("We are selling more shares!")
    variation_2 = input("How many shares are we selling today? (1-1000) ")
    if 1 <= int(variation_2) <= 1000:
        print(f"We are selling {variation_2} shares of {option_1} at ${current_stock_prices[option_1]:.2f} each.")
    else:
        print("Invalid number of shares. Please select a number between 1-1000.")


option_2 = input("Which stock holding would you like to trade second today?").lower().upper()
if option_2 in stock_options:
    print(f"You have selected {option_2}. The current price is ${current_stock_prices[option_2]:.2f}.")
else:
    print("Invalid stock option. Please select a valid stock from the list!")

choice_2 = input("Are we purchasing calls or puts today? (calls/puts) ")
if choice_2 == 'calls':
    print("We are buying calls!")
    variation_1 = input("How many call options are we purchasing today? (1-100) ")
    if 1 <= int(variation_1) <= 100:
        print(f"We are purchasing {variation_1} calls of {option_2} at ${current_stock_prices[option_2]:.2f} each.")
    else:
        print("Invalid number of call options. Please select a number between 1-100 to fill your order!")
elif choice_2 == 'puts':
    print("We are buying puts!")
    variation_2 = input("How many puts are we buying today? (1-100) ")
    if 1 <= int(variation_2) <= 100:
        print(f"We are purchasing {variation_2} puts of {option_2} at ${current_stock_prices[option_2]:.2f} each.")
    else:
        print("Invalid number of put options. Please select a number between 1-100 to fill your order!")


option_3 = input("Which stock holding would you like to trade third today?").lower().upper()
if option_3 in stock_options:
    print(f"You have selected {option_3}. The current price is ${current_stock_prices[option_3]:.2f}.")
else:
    print("Invalid stock option. Please select a valid stock from the list!")

choice_3 = input(f"Are we adding {option_3} to our portfolio? (yes/no) ")
if choice_3 == 'yes':
    print(f"We are adding {option_3} to our portfolio!")
elif choice_3 == 'no':
    print(f"We are not adding {option_3} to our portfolio...")
else:
    print("Invalid option. Please select again.")


option_4 = input("Which stock holding would you like to trade fourth today?").lower().upper()
if option_4 in stock_options:
    print(f"You have selected {option_4}. The current price is ${current_stock_prices[option_4]:.2f}.")
else:
    print("Invalid stock option. Please select a valid stock from the list!")

choice_4 = input(f"Are we increasing or decreasing our position size for {option_4} today? (increase/decrease) ")
if choice_4 == 'incerease':
    print(f"We are increasing our postion size in {option_4} today!")
elif choice_4 == 'decrease':
    print(f"We are decreasing our position size in {option_4} today...")
else:
    print("Invalid option. Please select again!")


print("Thank you for playing the Stock Market Simulator!")
exit()



















   