def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if 20% or more."""
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for inputs
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate and display the final price
    final = calculate_discount(original_price, discount_percentage)

    if discount_percentage >= 20:
        print(f"Discount applied. Final price: ${final:.2f}")
    else:
        print(f"No discount applied. Final price: ${original_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for price and discount percentage.")
