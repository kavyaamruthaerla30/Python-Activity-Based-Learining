products = [
    ("P101", 50.0, 10),
    ("P102", 120.0, 3),
    ("P103", 75.0, 8),
]

total_value = 0
for product_id, price, quantity in products:
    value = price * quantity
    total_value += value
    print(f"{product_id}: stock value = Rs. {value:.2f}")
    if quantity < 5:
        print("Reorder required for", product_id)

print(f"Total inventory value: Rs. {total_value:.2f}")
