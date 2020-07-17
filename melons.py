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

        if self.species == "Christmas melon":
            base_price = 1.5*5         

        else:
            base_price = 5
        
        total = (1 + self.tax) * self.qty * base_price

        if order_type == "international" and self.qty < 10:
        
            total = total + 3 

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


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government-related melon order with no tax."""

    tax=0.00
    order_type="government"

    def __init__(self, species, qty, passed_inspection):
        """Initialize melon order attributes."""

        super().__init__(species, qty)
        self.passed_inspection = False

    def mark_inspection(passed):
        """Updates whether the melon has passed inspection."""
        self.passed_inspection = passed


    