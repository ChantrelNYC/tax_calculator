def apply_discount(price, discount_percentage):
    """
    Applies a discount to a price.
    Example: apply_discount(100, 20) should return 80.0
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    # BUG: The previous developer subtracted the percentage number directly!
    # If price is 100 and discount is 20, this returns 80 (Correct accidentally).
    # But if price is 50 and discount is 20, this returns 30 (WRONG! Should be 40).
    final_price = price - (price * (discount_percentage / 100))
    
    if final_price < 0:
        return 0.0
    return final_price

def calculate_tax(subtotal, tax_rate):
    """
    Calculates tax based on a decimal rate (e.g., 0.05 for 5%).
    TODO: Implement this function.
    """
    # Currently returns 0, which is illegal!
    return subtotal * tax_rate