print("-----------------------------------")
print("Shopping Cart Validation")
print("-----------------------------------")

ItemsinCart = 0  # initialize variable


def add_to_cart(items_to_add):
    global ItemsinCart

    # check for negative input
    if items_to_add < 0:
        raise Exception("Cannot add a negative number of items.")

    # check cart limit (total should not exceed 5)
    if ItemsinCart + items_to_add > 5:
        raise Exception("Cart limit exceeded.")

    # add items to cart
    ItemsinCart += items_to_add
    print(f"{items_to_add} items added. Total in cart: {ItemsinCart}")


try:
    add_to_cart(2)
except Exception as e:
    print(e)

try:
    add_to_cart(-1)
except Exception as e:
    print(e)

try:
    add_to_cart(7)
except Exception as e:
    print(e)
