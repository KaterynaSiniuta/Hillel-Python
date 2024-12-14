class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

    def __str__(self):
        result = f"User: {self.user}\nItems:\n"
        for item, cnt in self.products.items():
            result += f"{item.name}: {cnt} pcs.\n"
        result += f"Total: {self.get_total()}"
        return result


lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")

print(lemon)

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)

assert isinstance(cart.user, User) is True
assert cart.get_total() == 60
assert cart.get_total() == 60

cart.add_item(apple, 10)
print(cart)

assert cart.get_total() == 80
