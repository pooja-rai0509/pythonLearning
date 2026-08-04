class ChaiOrder:
    def __init__(self, tea_type, swwetness, size):
        self.tea_type = tea_type
        self.swwetness = swwetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)

class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]

order1 = ChaiOrder.from_dict({"tea_type":"masala", "sweetness":"medium", "size":"large"})

order2 = ChaiOrder.from_string("Ginger-low-medium")

order3 = ChaiOrder("clove", "nice", "small")

print(order1)
print(order1.__dict__)
print(order2)
print(order2.__dict__)
print(order3)
print(order3.__dict__)