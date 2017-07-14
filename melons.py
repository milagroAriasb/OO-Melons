"""Classes for melon orders."""

import random

from datetime import datetime

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        if qty <= 100:
            self.qty = qty
        else:
            raise TooManyMelonsError("No more than 100 melons!")
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        """Returns a random number between 5 and 9."""

        total = random.randint(5, 9)

        today = datetime.now()

        # if time is 8-10:59am and weekday is Monday-Friday, $4 will be added
        # to the total
        if today.hour in range(8, 11) and today.weekday() in range(0, 5):

            total = total + 4

        return total

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas melons":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        super(DomesticMelonOrder, self).__init__(species, qty, "Domestic", 0.08)


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        super(InternationalMelonOrder, self).__init__(species, qty, "International", 0.17)
        self.country_code = country_code

    def get_total(self):
        """Calculate price, including tax."""

        total = super(InternationalMelonOrder,self).get_total()

        if self.qty < 10:
            total = total + 3
        
        return total 

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A US Government melon order."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        tax = 0.0
        super(GovernmentMelonOrder, self).__init__(species, qty, "Domestic", tax)
        self.passed_inspection = False

    def mark_inspection(self, passed):
        """Updates whether or not melon has passed inspection."""

        if type(passed) != type(True):
            raise ValueError("Need to pass a boolean type.")
        self.passed_inspection = passed


class TooManyMelonsError(ValueError):
    """Too many melons error."""
    pass
    