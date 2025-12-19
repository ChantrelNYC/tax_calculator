def apply_discount(price, discount_percentage):
    """
    Applies a discount to a price.
    Example: apply_discount(100, 20) should return 80.0
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    # Correct Logic: price * (percentage / 100) gives the amount to subtract
    final_price = price - (price * (discount_percentage / 100))
    
    return max(0.0, final_price)

def calculate_tax(subtotal, tax_rate):
    """
    Calculates tax based on a decimal rate (e.g., 0.05 for 5%).
    """
    if tax_rate < 0:
        raise ValueError("Tax rate cannot be negative")
        
    # Implementation: subtotal multiplied by the decimal rate
    return subtotal * tax_rate
