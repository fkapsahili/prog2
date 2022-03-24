conversions_CHF = {"CHF": 1.000, "EUR": 0.97, "GBP": 0.81, "MDL": 19.58}


source_currency = input("Please enter your source currency: ")
source_amount = input("Please enter your source amount: ")
target_currency = input("Please enter your target currency: ")

target_amount = source_amount / conversions_CHF[source_amount] * conversions_CHF[target_currency]

print("{target_currency}", target_amount)
