"""Basic template"""

from string import Template


def main():
    """creating and using template"""
    cart = []

    cart.append(dict(iteam="Milk", price=10, qty=2))
    cart.append(dict(iteam="Apples", price=8, qty=16))
    cart.append(dict(iteam="Carrots", price=5, qty=20))

    temp = Template("$qty x $iteam = $price")

    print("Cart: ")
    total = 0

    for iteam in cart:
        print(" ", temp.substitute(iteam))
        total += iteam["price"]

    print("Total: $%.2f" % total)


if __name__ == "__main__":
    main()
