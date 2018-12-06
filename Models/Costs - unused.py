class Costs(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return "{},{}".format(self.name, self.price)

    def __repr_(self):
        return self.__str__()

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price