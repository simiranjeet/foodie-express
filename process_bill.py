# def calculate_tax(amount):
#     return 0.05 if amount <= 4.00 else 0.13

# def round_cash_payment(amount):
#     return round(amount * 20) / 20.0  # Round to nearest nickel

# def process_payment(amount, payment_method):
#     try:
#         amount = float(amount)
#         if payment_method not in ["CASH", "DEBIT", "CREDIT"]:
#             raise ValueError("Invalid payment method")
        
#         # Calculate tax and total amount
#         tax_rate = calculate_tax(amount)
#         total = amount * (1 + tax_rate)
        
#         if payment_method == "CASH":
#             rounded_total = round_cash_payment(total)
#         else:
#             rounded_total = total

#         # Prepare the result string
#         result = (
#             f"Original Amount: {amount:.2f}<br>"
#             f"Total with Tax:  {total:.2f}<br>"
#             f"Rounded Amount:  {rounded_total:.2f}<br>"
#             f"Payment Method:  {payment_method}"
#         )
#         return result
#     except ValueError as e:
#         return str(e)


def calculate_tax(amount):
    return 0.05 if amount <= 4.00 else 0.13

def round_cash_payment(amount):
    return round(amount * 20) / 20.0  # Round to nearest nickel

def process_payment(amount, payment_method):
    try:
        amount = float(amount)
        if payment_method not in ["CASH", "DEBIT", "CREDIT"]:
            raise ValueError("Invalid payment method")
        
        # Calculate tax and total amount
        tax_rate = calculate_tax(amount)
        total = amount * (1 + tax_rate)
        
        if payment_method == "CASH":
            rounded_total = round_cash_payment(total)
        else:
            rounded_total = total

        # Prepare the result string
        result = (
            f"Original Amount: {amount:.2f}<br>"
            f"Total with Tax:  {total:.2f}<br>"
            f"Rounded Amount:  {rounded_total:.2f}<br>"
            f"Payment Method:  {payment_method}"
        )
        return result
    except ValueError as e:
        return str(e)
