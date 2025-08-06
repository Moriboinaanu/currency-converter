# Currency Converter in Python - Improved Command Line Version

from colorama import init, Fore, Style
init(autoreset=True)

def convert_currency(amount, from_currency, to_currency):
    # Exchange rates (base: USD)
    rates = {
        'USD': 1.0,
        'INR': 83.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'JPY': 146.5
    }

    if from_currency not in rates or to_currency not in rates:
        print(Fore.RED + "❌ Unsupported currency code entered!")
        return None

    # Convert to USD first, then to target currency
    amount_in_usd = amount / rates[from_currency]
    converted_amount = amount_in_usd * rates[to_currency]
    return converted_amount

def display_supported_currencies():
    print(Fore.CYAN + "\n📌 Supported Currencies:")
    print(Fore.YELLOW + " USD - US Dollar\n INR - Indian Rupee\n EUR - Euro\n GBP - British Pound\n JPY - Japanese Yen\n")

def main():
    print(Fore.GREEN + "\n==============================")
    print(Fore.GREEN + "💱 Welcome to Currency Converter")
    print(Fore.GREEN + "==============================")
    
    display_supported_currencies()

    from_currency = input(Fore.BLUE + "Enter FROM currency code (e.g. INR): ").strip().upper()
    to_currency = input(Fore.BLUE + "Enter TO currency code (e.g. USD): ").strip().upper()

    try:
        amount = float(input(Fore.BLUE + "Enter amount to convert: "))
        if amount <= 0:
            print(Fore.RED + "❌ Amount should be greater than zero.")
            return
    except ValueError:
        print(Fore.RED + "❌ Invalid amount. Please enter a number.")
        return

    result = convert_currency(amount, from_currency, to_currency)

    if result is not None:
        print(Fore.GREEN + f"\n✅ {amount} {from_currency} = {round(result, 2)} {to_currency}")
        print(Fore.MAGENTA + "Thank you for using the Currency Converter!\n")

if __name__ == "__main__":
    main()
