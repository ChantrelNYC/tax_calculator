def apply_discount(price, discount_percent):
    """
    Calculates the price after applying a percentage discount.
    """
    # Fix: Subtract the percentage of the price, not a flat amount
    return price - (price * (discount_percent / 100))

def calculate_tax(subtotal, tax_rate):
    """
    Calculates tax based on the subtotal and rate.
    """
    # Implementation: multiply subtotal by the tax rate
    return subtotal * tax_rate
