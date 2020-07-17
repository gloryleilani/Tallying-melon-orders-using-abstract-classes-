"""Classes for melon orders."""


class AbstractMelonOrder:
    """An abstraact base class that other melon orders inherit from."""

    #These data will appear in the classes for domestic and int'l melon orders
    tax = 0.00
    order_type = None

    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False
        

    def get_total(self):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total


    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax=0.08
    order_type="domestic"

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super().__init__(species, qty)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax=0.17
    order_type="international"

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

