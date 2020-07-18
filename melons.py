
import random
from datetime import datetime, time
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
        

    def get_base_price(self):
        """Determine the base price for melons."""

        #Gets current time stamp to determine if rush hour pricing applies
        #timestamp = datetime.now() 
        #Sample result is "datetime.datetime(2020, 7, 17, 23, 42, 3, 970250)

        timestamp = datetime.now()
        print("Order timestamp:", timestamp)  
        
        #class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
        #datetime.weekday() returns the day of the week as an integer, where Monday is 0 and Sunday is 6. 

        start = 8 
        end = 11
        
        

        if (start < timestamp.hour < end) and datetime.weekday(timestamp)<6:
            base_price = 4 + random.randint(5,9) #Handle splurge pricing
        
        else:
            base_price = random.randint(5,9) #Handle splurge pricing

        #Prints the timestamp after it's converted to local time.  
        #print("Order timestamp:", datetime.fromtimestamp(timestamp))


        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melon":
            base_price = 1.5*base_price         

        else:
        
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


    