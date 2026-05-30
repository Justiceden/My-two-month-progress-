from enum import Enum, auto

class DiscountTypes(Enum):
    SEASONAL = auto()
    STANDARD = auto()
    WEIGHT = auto()


class Discount:
    def __init__(self, seasonal, standard):
        self.seasonal = seasonal
        self.standard = standard

    def get_discount(self, discount_type, weight=0):
        if discount_type == DiscountTypes.SEASONAL:
            return self.seasonal
        
        elif discount_type == DiscountTypes.STANDARD:
            return self.standard
        
        elif discount_type == DiscountTypes.WEIGHT:
            if weight <= 10:
                return 6
            else:
                return 18

    def apply_discount(self, price, discount_type, weight=0):
        discount = self.get_discount(discount_type, weight)
        final_price = price * (1 - discount / 100)
        return final_price


# Create object
potato = Discount(12, 6)

# Test
print(potato.apply_discount(100, DiscountTypes.WEIGHT, 15))  # 82







    





















