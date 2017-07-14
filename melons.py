"""Classes for melon orders."""

import random

class AbstractMelonOrder(object):
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, species, qty, order_type, tax):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = order_type
        self.tax = tax

    def get_base_price(self):
        """Returns a random number between 5 and 9."""

        return random.randint(5, 9)

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