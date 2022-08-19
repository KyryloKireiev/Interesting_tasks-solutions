class SuperShop:

    def __init__(self, name):
        self.name = name
        self.goods = list()

    def add_product(self, product):
        self.goods.append(product)

    def remove_product(self, product):
        self.goods.remove(product)


class StringValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.verify(value):
            setattr(instance, self.name, value)

    @staticmethod
    def verify(name):
        if type(name) is str and 2 <= len(name) <= 50:
            return True
        return False


class PriceValue:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if self.verify(value):
            setattr(instance, self.name, value)

    @staticmethod
    def verify(price):
        if type(price) in (int, float) and 0 <= price <= 10000:
            return True
        return False


class Product:

    name = StringValue()
    price = PriceValue()

    def __init__(self, name, price):
        self.name = name
        self.price = price


shop = SuperShop("У Балакирева")
shop.add_product(Product("Курс по Python", 0))
shop.add_product(Product("Курс по Python ООП", 2000))
for p in shop.goods:
    print(f"{p.name}: {p.price}")

shop.add_product(Product("tdsf", 23))

for p in shop.goods:
    print(f"{p.name}: {p.price}")
