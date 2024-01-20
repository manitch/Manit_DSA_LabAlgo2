def find_transactions_to_achieve_target(transactions, daily_target):
    total = 0
    for i, transaction in enumerate(transactions):
        total += transaction
        if total >= daily_target:
            return i + 1
    return -1

# Time complexity: O(n)
# Space complexity: O(1)




# Travellers payment 

def payment_approach(currencies, amount):
    currencies.sort(reverse=True)
    result = []

    for currency in currencies:
        notes = amount // currency
        amount %= currency
        result.append(f"{currency}:{notes}")

    print("Your payment approach in order to give the minimum number of notes will be")
    print("\n".join(result))

# Time complexity: O(n log n) due to sorting
# Space complexity: O(1)
