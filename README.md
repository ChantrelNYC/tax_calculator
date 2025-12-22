# 🛒 Lab: The Shopping Cart Logic Fix

**Scenario:** We have a discount function that works _sometimes_ (try testing it with the number 100), but customers are complaining that the math is wrong for other prices. Also, the tax calculator is completely missing.

**Your Job:** Fork the repo, fix the math, implement the tax feature, and pass the GitHub Action check.

### **Instructions:**

1.  **Fork & Clone** the repository.
2.  **Create a Branch:** `git checkout -b fix/discount-logic`
3.  **Run Tests Locally:** `python -m unittest discover tests`
    - _Observation:_ You will see `AssertionError: 30.0 != 40.0`. Read the error message carefully!
4.  **Fix `src/cart.py`:**
    - **Step A:** Change the `apply_discount` logic. It currently does `price - discount_percentage`. It _should_ calculate `price - (price * (discount_percentage / 100))`.
    - **Step B:** Implement `calculate_tax` so it returns `subtotal * tax_rate`.
5.  **Commit & Push:**
    ```bash
    git commit -am "fix: corrected percent math and added tax calc"
    git push origin fix/discount-logic
    ```
6.  **Open Pull Request:**
    - Watch the "Cart Logic Checker" run.
    - If it turns Green ✅, you are done.
